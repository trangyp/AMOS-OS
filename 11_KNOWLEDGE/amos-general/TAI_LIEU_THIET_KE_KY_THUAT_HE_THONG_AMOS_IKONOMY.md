---
title: TAI LIEU THIET KE KY THUAT HE THONG AMOS IKONOMY
tags: [amos-general, amos, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture

---


# **TÀI LIỆU THIẾT KẾ KỸ THUẬT HỆ THỐNG AMOS–IKONOMY**
**(So với thiết kế IKONOMY ban đầu và mặt bằng công nghệ hiện hành)**
**Phiên bản:** 1.0
**Phạm vi:** 01 mô-đun điện phân nước công suất nhỏ (≈1 kW) và lớp điều khiển AMOS
**Mục đích tài liệu:** thiết kế – sản xuất – tích hợp – thẩm định – triển khai thực tế
AMOS-IKONOMY được đánh giá là dẫn đầu trong phân khúc module vì **đồng thời đạt được các yếu tố vốn mâu thuẫn nhau** :
  1. Hiệu suất điện năng cao, gần trần vật lý.


  2. Tuổi thọ dài hơn đáng kể so với cùng cấu hình.


  3. Uptime ≥98% trong điều kiện thực tế.


  4. Chi phí vòng đời thấp hơn 25–40%.


  5. Có thể triển khai tại các khu vực khó, không yêu cầu hạ tầng phức tạp.


  6. Mức độ an toàn cao, giảm rủi ro xã hội và truyền thông.


Hầu hết hệ thống khác chỉ tối ưu **một hoặc hai** yếu tố trong số trên.
AMOS-IKONOMY tối ưu **toàn bộ cùng lúc** nhờ logic điều khiển AMOS. AMOS-IKONOMY không phá vỡ định luật Faraday và không vượt giới hạn nhiệt động học. Giá trị vượt trội của hệ thống nằm ở việc **chuyển giới hạn vật lý và giới hạn con người thành luật điều khiển bắt buộc** , giúp hệ thống:
  * vận hành sát trần vật lý nhưng không vượt ngưỡng an toàn,


  * duy trì hiệu quả trong thời gian dài,


  * và phù hợp với điều kiện triển khai tại Việt Nam.


Đây chính là lý do AMOS-IKONOMY **vượt trội so với IKONOMY nguyên bản và các hệ thống điện phân module hiện có trên thị trường**.
* * *
## **1\. Tổng quan kỹ thuật**
AMOS–IKONOMY là hệ thống sản xuất hydro bằng điện phân nước, cấu hình **mô-đun công suất nhỏ** , thiết kế cho vận hành liên tục trong điều kiện thực tế.
Hệ thống hướng tới các điều kiện biên sau:
  * nguồn điện DC dao động trong dải 48–96 V,


  * môi trường vận hành không được kiểm soát chặt,


  * nhân lực vận hành hạn chế,


  * yêu cầu an toàn và độ tin cậy cao.


AMOS–IKONOMY **không thay đổi phản ứng điện hóa cơ bản** của quá trình điện phân nước. Khác biệt kỹ thuật của hệ thống nằm ở:
  * kiến trúc điều khiển dựa trên giới hạn vật lý,


  * cơ chế giám sát suy giảm theo xu hướng thời gian,


  * cơ chế tự bảo vệ chủ động trong toàn bộ vòng đời vận hành.


Hệ thống được thiết kế để đáp ứng đồng thời ba mục tiêu kỹ thuật sau:
  1. **Sản lượng:** sản lượng hydro tỷ lệ trực tiếp với dòng điện và tiệm cận giới hạn vật lý ứng với công suất điện cấp vào.


  2. **Độ bền:** suy giảm điện hóa được theo dõi định lượng và được điều tiết chủ động nhằm kéo dài tuổi thọ hữu dụng của stack.


  3. **An toàn:** giảm tối đa phụ thuộc vào phản ứng kịp thời của người vận hành; ưu tiên cơ chế giảm tải có kiểm soát thay cho ngắt đột ngột.


```
    flowchart TB
      A[Nguon DC 48-96 VDC] --> B[Bao ve nguon: qua ap, thap ap, dao cuc, han dong khoi dong, TVS, LC]
      B --> C[Loc EMI EMC: tach mass tin hieu va cong suat, noi dat khung]
      C --> D[Khoi cong suat Cannon: Buck hoac Buck-Boost dong bo, dieu khien theo dong]
      D --> E[Cam bien dong: Hall hoac Shunt + ADC]
      D --> F[Cam bien ap Stack: tong ap, tuy chon do theo doan]
      D --> G[Driver cong: gioi han toc do canh, dieu chinh dead-time]
      D --> H[Stack dien phan: cell plate bar]
      H --> I[Khoi nhiet: tam phan bo nhiet, khoi tich nhiet, duong lam mat]
      I --> J[Cam bien nhiet do: T1 T2 T3]
      H --> K[Khoi tach khi: tach H2 va O2]
      K --> L[Bubbler Bay nuoc Loc khi: thiet ke chiu luu luong boost]
      L --> M[Van dieu ap va van an toan H2]
      M --> N[Ngo ra khi H2]
      K --> O[Cam bien ap suat: P_trung_binh va gợn_ap]
      H --> P[He thong nuoc: bon cap hoi]
      P --> Q[Cam bien muc nuoc]
      P --> R[Cam bien do dan dien: tuy chon]
    
      subgraph MCU[Vi dieu khien thoi gian thuc]
        S[Vong dieu khien nhanh 0.1-1 kHz: PI dong + feedforward, gioi han dI dt, ramp]
        T[Thu vien dang song: DC muot, DC xung, burst mem]
      end
    
      E --> S
      F --> S
      T --> S
      S --> G
    
      subgraph AMOS[Lop loi AMOS]
        U[Uoc luong trang thai: T_tb, dT dt, deltaT, R_eq, dR dt, chi so tro khang]
        V[Tich luy suy giam: D_index, ngan sach boost]
        W[Quan ly phong bi van hanh: on dinh, boost, suy giam, bao ve]
        X[Khoi quyet dinh: cap boost, tu choi, giam tai]
      end
    
      J --> U
      O --> U
      Q --> U
      R --> U
      S --> U
      U --> V
      V --> X
      X --> W
      W --> T
    
      subgraph GIAMSAT[Lop giam sat va kiem toan]
        Y[Ghi log va truy vet: su kien, nguong, ly do]
        Z[Giam sat tu xa tuy chon: cau hinh, bao cao]
        AA[Goi kiem toan: uptime, so lan can thiep, lich su boost, xu huong D_index]
      end
    
      X --> Y
      U --> Y
      W --> Y
      Y --> AA
      Z --> Y
```
## **2\. Kiến trúc tổng thể hệ thống**
### **2.1 Chuỗi chức năng**
Hệ thống AMOS–IKONOMY được tổ chức theo chuỗi chức năng cố định:
Nguồn DC 48–96 VDC
→ Khối điều hòa và bảo vệ nguồn
→ Khối điều khiển dòng điện Cannon
→ Stack điện phân
→ Hệ thống quản lý nhiệt
→ Hệ thống tách và điều hòa khí
→ Ngõ ra hydro
Chuỗi chức năng này là **bắt buộc** và không được thay đổi trong thiết kế tích hợp.
### **2.2 Nguyên tắc kiến trúc bắt buộc**
  1. **Không điều khiển trực tiếp stack theo nhu cầu sản lượng.**
Mọi yêu cầu tăng hoặc giảm sản lượng hydro phải được chuyển đổi thành yêu cầu d òng điện và xử lý qua lớp điều khiển trung gian.


  2. **Mọi thay đổi dòng điện phải tuân thủ đồng thời các giới hạn sau:**
     * giới hạn điện: dòng, tốc độ thay đổi dòng, điều kiện nguồn,
     * giới hạn nhiệt: nhiệt độ tuyệt đối, tốc độ tăng nhiệt, gradient nhiệt,
     * giới hạn khí: áp suất, dao động áp suất, ổn định lưu lượng,
     * giới hạn suy giảm: xu hướng điện áp và điện trở theo thời gian.


  3. **Ưu tiên bảo toàn stack và an toàn hệ thống.**
Trong mọi tình huống xung đột giữa sản lượng tức thời và rủi ro suy giảm hoặc rủi ro an toàn, hệ thống bắt buộc lựa chọn phương án giảm tải.


```
                         HE THONG AMOS-IKONOMY (Kien truc tong the)
    
     [1] NGUON DC 48-96V
            |
            v
     [2] BAO VE + DIEU HOA NGUON
         - Qua ap / thap ap (OVP/UVP)
         - Dao cuc
         - Han dong khoi dong (inrush)
         - Chong xung (TVS)
         - Loc dau vao (LC)
            |
            v
     [3] LOC EMI/EMC + NOI DAT
         - Tach mass tin hieu / mass cong suat
         - Noi dat khung may, bo tri day dan dung quy tac
            |
            v
     [4] KHOI CONG SUAT "CANNON" (BO BIEN DOI THEO DONG)
         - Buck / Buck-Boost dong bo
         - Dieu khien vong kin theo dong (current-mode)
         - Gioi han toc do tang dong (dI/dt) + ramp
         - Dieu chinh dead-time + gioi han canh xung (slew-rate)
            |
            |------------------------------\
            |                               \
            v                                v
     [4a] CAM BIEN DONG                    [4b] CAM BIEN AP STACK
         - Hall hoac Shunt + ADC               - Tong ap
         - Do chinh xac muc tieu <= 1%         - Tuy chon do theo doan (segment)
            |                               /
            |                              /
            \-------------\    /----------/
                          v  v
                   [5] MCU THOI GIAN THUC (0.1-1 kHz)
                       - PI dieu khien dong + feed-forward
                       - Gioi han dI/dt, ramp, gioi han cong suat
                       - Thu vien dang song:
                           (a) DC muot (on dinh)
                           (b) DC xung (giam bam bot khi)
                           (c) Burst mem (boost co gioi han)
                          |
                          v
                 [6] DRIVER CONG (gate driver)
                     - Tao xung dieu khien MOSFET/SiC
                     - Kiem soat dead-time, slew-rate
                          |
                          v
     [7] STACK DIEN PHAN (vung phan ung)
         - Cell / plate / bar (tuy cau hinh)
         - Sinh khi H2 va O2
            |
            |------------------------\
            |                         \
            v                          v
     [8] HE THONG NHIET               [9] HE THONG NUOC
         - Tam phan bo nhiet              - Bon nuoc, cap/hoi
         - Khoi tich nhiet                - Cam bien muc nuoc
         - Duong lam mat                  - Tuy chon cam bien do dan dien
         - Cam bien nhiet do T1 T2 T3     - Logic: nuoc kem => giam tai
            |                         /
            |                        /
            \-----------\   /--------/
                        v v
                   [10] AMOS CORE (lop quyet dinh)
                       A. Uoc luong trang thai
                          - T_avg, dT/dt, deltaT
                          - R_eq, dR_eq/dt (xu huong suy giam)
                          - P, do gon ap, on dinh khi
                       B. Tich luy suy giam
                          - D_index (chi so suy giam)
                          - Ngan sach boost (boost budget)
                       C. Quan ly phong bi van hanh (envelope)
                          - On dinh (cruise)
                          - Boost (gioi han thoi gian + cooldown)
                          - Suy giam (degraded)
                          - Bao ve (protective)
                          - Khoa (lockout)
                       D. Logic quyet dinh
                          - Cap boost neu tat ca nguong dat
                          - Tu choi boost neu bat ky nguong vi pham
                          - Giam tai som, khong doi den cat khan cap
                        |
                        v
                 (Lenh dieu khien tra ve MCU)
         "Chon dang song" + "Muc dong muc tieu" + "Gioi han thoi gian"
    
            |
            v
     [11] HE THONG TACH VA DIEU HOA KHI
         - Tach H2 / O2
         - Bubbler / bay nuoc / loc khi (chiu duoc luu luong boost)
         - Cam bien ap suat (P trung binh, do gon ap)
         - Van dieu ap / van an toan
            |
            v
     [12] NGO RA H2 (co dieu tiet)
         - Khong luu tru H2 khi dung may (theo triet ly an toan)
    
            |
            v
     [13] LOP GIAM SAT + KIEM TOAN (tuy chon)
         - Ghi log va truy vet: su kien, nguong, ly do
         - Giam sat tu xa: cau hinh, bao cao
         - Goi kiem toan: uptime, so lan can thiep, lich su boost, xu huong D_index
```
## **1) Sơ đồ luồng dữ liệu (Data Flow Diagram)**
```
                        SO DO LUONG DU LIEU (AMOS-IKONOMY)
    
     CAM BIEN (INPUT)                         TANG DIEU KHIEN (CONTROL)                    TANG THUC THI (ACTUATION)
     ----------------                         -------------------------                    -------------------------
    
      Dong I_meas  ----------------------\
      Ap  V_stack  -----------------------\
      Nhiet T1,T2,T3 ----------------------->  [MCU VONG NHANH 0.1-1 kHz]  -----------------> [DRIVER CONG]
      Ap suat P, ripple -------------------/        - Dieu khien PI theo dong               - Dead-time
      Muc nuoc Level ---------------------/         - Gioi han dI/dt, ramp                  - Slew-rate
      Do dan Cond (tuy chon) ------------/          - Thuc thi waveform da duoc cap         - Gate timing
                                                     |
                                                     | (truyen telemetry / sample tong hop 1-10 Hz)
                                                     v
                                             [AMOS CORE 1-10 Hz]
                                              - Uoc luong trang thai (State Estimator)
                                              - Tinh chi so suy giam D_index
                                              - Tinh ngan sach boost (Boost budget)
                                              - Quan ly phong bi (Envelope Manager)
                                              - Logic ra quyet dinh (Decision Logic)
                                                     |
                                                     | (lenh dieu khien cap cao)
                                                     v
                                        LENH TU AMOS TRA VE MCU
                                        - I_set: dong muc tieu
                                        - waveform_id: loai dang song
                                        - boost_time_limit: gioi han thoi gian boost
                                        - cooldown_time: thoi gian hoi phuc bat buoc
                                        - envelope_mode: cruise / boost / degraded / protective / lockout
                                                     |
                                                     v
                                      [MCU AP DUNG LENH + KIEM TRA RANG BUOC]
                                      - Neu lenh vi pham nguong nhanh => tu choi / cat giam
                                      - Neu hop le => phat xung dieu khien khoi Cannon
                                                     |
                                                     v
                                        [KHOI CANNON + STACK DIEN PHAN]
                                        - Dong thuc thi I(t)
                                        - Sinh khi H2/O2
                                        - Phat sinh nhiet va dao dong ap
                                                     |
                                                     v
                                        [HE NHIET + HE KHI + HE NUOC]
                                        - Nhiet duoc truyen va giam gradient
                                        - Khi duoc tach va dieu hoa
                                        - Nuoc duoc cap va giam sat
                                                     |
                                                     v
                                        [LOGGER + TRUY VET + KIEM TOAN]
                                        - Luu: gia tri, su kien, nguong, ly do
                                        - Bao cao: uptime, can thiep, boost usage, D_index trend
```
### **Ghi chú kỹ thuật**
  * **MCU vòng nhanh** chịu trách nhiệm “phản xạ”: giữ dòng đúng, không rung, không sốc.


  * **AMOS** chịu trách nhiệm “quyết định”: có boost hay không, boost bao lâu, khi nào phải giảm tải trước khi hỏng.


  * **Logger/kiểm toán** ghi rõ “ai ra quyết định gì và vì sao”, để phục vụ thẩm định và chứng minh an toàn.


* * *
## **2) Sơ đồ trạng thái vận hành (State Machine)**
```
                             SO DO TRANG THAI VAN HANH (AMOS-IKONOMY)
    
     [OFF]
       |
       | Dieu kien: co nguon, tat ca cam bien hop le, muc nuoc dat, khong loi
       v
     [STARTUP - KHOI DONG AN TOAN]
       - Ramp dong tu 0 -> I_cruise theo dI/dt gioi han
       - Kiem tra nhiet, ap, on dinh trong cua so thoi gian
       |
       | Neu on dinh du thoi gian => vao CRUISE
       | Neu loi / bat thuong => vao PROTECTIVE hoac LOCKOUT
       v
     [CRUISE - VAN HANH ON DINH DAI HAN]
       - Muc tieu: san luong on dinh, suy giam thap, it can thiep
       - AMOS theo doi: T_avg, deltaT, dT/dt, R_eq, dR/dt, P_ripple, Level, Cond
       |
       | Neu co yeu cau tai cao (demand) VA tat ca nguong Boost OK
       v
     [BOOST - TANG CONG SUAT NGAN HAN]
       - I_set tang den I_boost theo ramp
       - Gioi han thoi gian: 30-180 s (do AMOS cap)
       - Theo doi sat: nhiet, gradient, ap, trinh trang dien hoa
       |
       | Ket thuc boost (het gio) HOAC bat ky nguong vi pham
       v
     [COOLDOWN - HOI PHUC BAT BUOC]
       - Dua dong ve I_cruise hoac thap hon
       - Giu trong thoi gian 5-10 phut
       - Muc tieu: dua T_avg, deltaT, P_ripple ve vung an toan
       |
       | Neu on dinh => quay lai CRUISE
       | Neu xau di => vao DEGRADED hoac PROTECTIVE
       v
    
     [DEGRADED - SUY GIAM CO KIEM SOAT]
       - Giam san luong de bao toan stack va tranh su co
       - Gioi han: I_max_deg < I_cruise
       - Chi cho phep hoat dong khi cac nguong toi thieu dat
       |
       | Neu phuc hoi du => quay lai CRUISE
       | Neu vi pham nguong an toan => PROTECTIVE
       v
    
     [PROTECTIVE - BAO VE]
       - Giam dong nhanh nhung co kiem soat (khong cat giat)
       - Co the dua ve muc an toan thap hoac dung co trinh tu
       |
       | Neu su co lap lai qua so lan trong cua so thoi gian
       v
    
     [LOCKOUT - KHOA AN TOAN]
       - Tu choi boost
       - Tu choi khoi dong lai ngay lap tuc
       - Bat buoc cooldown / kiem tra / thao tac reset theo quy trinh
       |
       | Sau khi dat dieu kien reset (thoi gian, nhiet, muc nuoc, loi cleared)
       v
     [STARTUP - KHOI DONG AN TOAN]
```
### **Bảng điều kiện chuyển trạng thái (rõ ràng, dễ audit)**
```
    CRUISE -> BOOST
      Dieu kien bat buoc (tat ca):
      - T_avg trong 55-75 C
      - deltaT <= 5 C
      - dT/dt <= 1 C/phut
      - P trong 1.5-3 bar va P_ripple <= 3%
      - dR_eq/dt nho hon nguong (khong co xu huong suy giam nhanh)
      - Level OK, Cond trong nguong (neu co)
      - so lan boost trong cua so thoi gian chua vuot han
    
    BOOST -> COOLDOWN
      - Het boost_time_limit HOAC
      - Bat ky nguong nao vi pham HOAC
      - D_index tang nhanh (vuot nguong)
    
    BAT KY TRANG THAI -> PROTECTIVE
      - Vuot nguong an toan: nhiet qua cao, ap qua cao, dao dong ap lon
      - Cam bien khong dong thuan (sensor disagreement)
      - Loi phan cung cong suat (driver fault)
    
    PROTECTIVE -> LOCKOUT
      - Loi lap lai qua N lan trong M phut
      - De phong thao tac sai hoac co loi dai
```
## **3\. Nguyên lý thiết kế cốt lõi**
### **3.1. Nguyên lý điều khiển theo dòng điện**
Trong hệ thống điện phân nước, các đại lượng quyết định gồm: tốc độ sinh hydro, mức phân cực điện cực, tốc độ hình thành bọt khí và tốc độ suy giảm vật liệu. Các đại lượng này **phụ thuộc trực tiếp vào dòng điện và mật độ dòng điện** đi qua stack.
Điện áp đặt lên stack là kết quả của:
  * điện áp thuận nghịch,


  * tổn hao hoạt hóa,


  * tổn hao ohmic,


  * tổn hao truyền khối.


Điện áp **không phải** là biến điều khiển an toàn cho sản lượng hydro.
Các nguyên tắc thiết kế bắt buộc:
  * Không điều khiển công suất bằng cách tăng điện áp.


  * Không cưỡng bức dòng điện vượt ngưỡng thiết kế thông qua “đẩy áp”.


  * Chỉ cho phép điều khiển dòng điện theo thời gian, với tốc độ thay đổi và giá trị tuyệt đối bị giới hạn bởi các điều kiện vật lý của hệ thống.


Kết luận nguyên lý điều khiển:
  * **Dòng điện là biến điều khiển duy nhất đối với quá trình điện phân.**


  * **Điện áp chỉ được sử dụng làm biến giám sát và chẩn đoán trạng thái stack.**


### **3.2. Nguyên lý điều khiển liên hợp đa miền vật lý**
AMOS–IKONOMY không tách rời các miền điện, nhiệt và khí trong điều khiển. Ba miền này được xem là **một hệ liên hợp bắt buộc**.
Quan hệ nhân quả trong vận hành:
  * Tăng dòng điện → tăng tổn hao điện → tăng nhiệt độ stack.


  * Tăng nhiệt độ → thay đổi điện trở nội → tăng tốc độ suy giảm vật liệu.


  * Tăng tốc độ sinh khí → tăng dao động áp suất → tăng rủi ro an toàn.


Do đó, **mọi quyết định tăng dòng điện chỉ được phép thực hiện khi đồng thời thỏa mãn tất cả các điều kiện sau** :
  * Điều kiện nhiệt: nhiệt độ tuyệt đối, tốc độ tăng nhiệt và gradient nhiệt trong giới hạn cho phép.


  * Điều kiện khí: áp suất và dao động áp suất ổn định trong dải thiết kế.


  * Điều kiện suy giảm: xu hướng điện áp và điện trở nội không tăng nhanh theo thời gian.


  * Điều kiện lịch sử tải: mức độ stress tích lũy chưa vượt ngưỡng vận hành an toàn.


Luật điều khiển bắt buộc:
  * Nếu **bất kỳ một điều kiện nào không thỏa mãn** , hệ thống **bắt buộc giảm dòng điện**.


  * Không tồn tại ngoại lệ vì lý do sản lượng hoặc yêu cầu tức thời.


## **3\. Nguyên lý thiết kế cốt lõi**
### **3.1 Điều khiển theo dòng điện**
Trong điện phân nước, tốc độ sinh hydro và mức suy giảm vật liệu phụ thuộc trực tiếp vào dòng điện/mật độ dòng. Điện áp chủ yếu phản ánh trạng thái phân cực và điện trở nội, không phải biến điều khiển an toàn.
Nguyên tắc bắt buộc:
  * Không điều khiển công suất bằng cách “đẩy áp”.


  * Không cưỡng bức dòng vượt ngưỡng bằng điện áp.


  * Chỉ điều khiển dòng theo thời gian trong giới hạn vật lý xác định.


Kết luận nguyên lý:
  * **Dòng điện là biến điều khiển chính.**


  * **Điện áp là biến quan sát/chẩn đoán.**


### **3.2 Điều khiển liên hợp đa miền vật lý**
AMOS–IKONOMY coi điện–nhiệt–khí là một hệ liên hợp:
  * Tăng dòng → tăng tổn hao → tăng nhiệt.


  * Tăng nhiệt → thay đổi điện trở → tăng suy giảm.


  * Tăng sinh khí → tăng dao động áp → tăng rủi ro an toàn.


Mọi quyết định tăng dòng chỉ được phép khi đồng thời thỏa:
  * điều kiện nhiệt (nhiệt độ và gradient),


  * điều kiện khí (áp suất và dao động),


  * điều kiện suy giảm (xu hướng điện trở/phân cực),


  * điều kiện lịch sử tải (stress tích lũy).


Chỉ cần 1 điều kiện không đạt → giảm tải.
## **4\. Khối điều khiển công suất Cannon**
Khối Cannon là **bộ biến đổi công suất điều khiển theo dòng điện** , được thiết kế để **cấp dòng chính xác cho stack trong các giới hạn cho phép**. Khối này **không được thiết kế để tối đa hóa công suất** và **không có quyền vượt giới hạn vận hành**.
### **4.1. Chức năng bắt buộc**
  * Tạo và duy trì dòng điện theo giá trị đặt.


  * Ổn định dòng điện khi điện áp nguồn dao động trong dải cho phép.


  * Giới hạn động học dòng điện nhằm bảo vệ stack.


### **4.2. Ràng buộc thiết kế**
  * Bắt buộc sử dụng điều khiển dòng vòng kín.


  * Bắt buộc giới hạn tốc độ thay đổi dòng (dI/dt) để tránh:
    * sốc điện hóa,
    * sốc nhiệt,
    * tăng suy giảm không hồi phục.


  * Dòng điện đầu ra **không được vượt** các ngưỡng do hệ thống AMOS xác định.


  * Không cho phép bỏ qua, nới lỏng hoặc ghi đè giới hạn, **kể cả khi nguồn điện đầu vào còn dư công suất**.


Khối Cannon chỉ đóng vai trò **thực thi mệnh lệnh dòng điện trong phong bì cho phép** , không tham gia ra quyết định tăng tải.
## **5\. Stack điện phân và các vùng vận hành**
Stack điện phân được vận hành theo các vùng dòng điện đã được xác định trước, dựa trên đặc tính nhiệt, đặc tính suy giảm và yêu cầu an toàn.
### **5.1. Vùng vận hành ổn định dài hạn**
Vùng vận hành ổn định được định nghĩa bởi các điều kiện sau:
  * Mật độ dòng điện thấp hơn ngưỡng gây suy giảm nhanh.


  * Nhiệt độ vận hành và gradient nhiệt nằm trong giới hạn thiết kế.


  * Xu hướng điện áp và điện trở nội ổn định theo thời gian.


Đặc tính vận hành:
  * Cho phép vận hành liên tục dài hạn.


  * Ít yêu cầu can thiệp của người vận hành.


  * Là vùng vận hành mặc định của hệ thống.


### **5.2. Vùng tăng công suất ngắn hạn (Boost)**
Vùng tăng công suất chỉ được phép kích hoạt khi **đồng thời thỏa mãn tất cả các điều kiện sau** :
  * Hệ thống còn dư địa nhiệt (nhiệt độ tuyệt đối và tốc độ tăng nhiệt dưới ngưỡng).


  * Không xuất hiện xu hướng tăng nhanh của điện áp hoặc điện trở nội.


  * Áp suất và dao động áp suất khí nằm trong dải cho phép.


  * Tần suất và mật độ boost chưa vượt ngưỡng vận hành an toàn.


Quy tắc bắt buộc:
  * Boost chỉ được phép trong thời gian giới hạn.


  * Không cho phép các chu kỳ boost liên tiếp với mật độ cao.


  * Khi bất kỳ điều kiện nào không còn thỏa mãn, hệ thống **bắt buộc tự động quay về vùng vận hành ổn định**.


## **6\. Lớp điều khiển AMOS**
AMOS là **lớp logic điều khiển quyết định** của toàn bộ hệ thống AMOS–IKONOMY. AMOS được xây dựng trên **các luật vật lý, luật suy giảm vật liệu và kinh nghiệm vận hành** , **không phải** hệ thống học máy thích nghi tự do. AMOS không “tối ưu theo mục tiêu tức thời”, mà **đánh giá trạng thái vận hành tổng thể theo thời gian**.
### **6.1. Các đại lượng giám sát bắt buộc**
AMOS liên tục giám sát và cập nhật các đại lượng sau:
  * Nhiệt độ stack và **tốc độ tăng nhiệt theo thời gian (dT/dt)**.


  * Gradient nhiệt trong stack.


  * Điện áp stack và **xu hướng biến thiên theo thời gian**.


  * Điện trở tương đương của stack và **tốc độ tăng điện trở (dR/dt)**.


  * Áp suất khí hydro và mức dao động áp suất.


  * Lịch sử vận hành: số lần boost, thời gian boost, và **stress tích lũy**.


AMOS **không ra quyết định dựa trên giá trị tức thời** , mà dựa trên **xu hướng và tốc độ biến đổi** của các đại lượng trên.
### **6.2. Nguyên tắc ra quyết định**
Nguyên tắc điều khiển cốt lõi của AMOS được xác định như sau:
  * Nếu một hành động làm tăng sản lượng hydro trong ngắn hạn **nhưng làm tăng xác suất suy giảm hoặc hư hỏng trong tương lai** , hành động đó **không được cho phép**.


  * Khi xuất hiện xung đột giữa sản lượng tức thời và độ bền/an toàn, AMOS **bắt buộc ưu tiên bảo toàn hệ thống**.


Chiến lược bảo vệ chính:
  * **Giảm tải sớm, có kiểm soát** (derating chủ động).


  * Tránh tối đa cơ chế **cắt khẩn cấp (shutdown)** trừ trường hợp vượt ngưỡng an toàn tuyệt đối.


AMOS được thiết kế để **ngăn sự cố trước khi xảy ra** , không chỉ phản ứng khi sự cố đã hình thành.
## **7\. So sánh với thiết kế IKONOMY ban đầu**
### **7.1. Hạn chế của thiết kế IKONOMY ban đầu**
Thiết kế IKONOMY ban đầu tập trung mạnh vào:
  * phần cứng công suất,


  * khả năng tạo dạng dòng điện đặc biệt.


Tuy nhiên, trong vận hành thực tế, hệ thống bộc lộ các hạn chế sau:
  * Phụ thuộc lớn vào kinh nghiệm và phản ứng của người vận hành.


  * Nhiều tình huống yêu cầu can thiệp thủ công khi xuất hiện dấu hiệu bất thường.


  * Cơ chế bảo vệ chủ yếu dựa trên **ngưỡng cắt cứng** , dẫn đến dừng hệ thống đột ngột và stress nhiệt – điện cao.


### **7.2. Thay đổi cấp kiến trúc của AMOS–IKONOMY**
AMOS–IKONOMY thay đổi cách tiếp cận ở **cấp kiến trúc hệ thống** , không phải tinh chỉnh cục bộ:
  * Các giới hạn vật lý (dòng, nhiệt, suy giảm, khí) được **đưa trực tiếp vào lõi logic quyết định**.


  * Quyền “ép chạy” của con người bị loại bỏ khỏi chuỗi điều khiển.


  * Cơ chế bảo vệ chuyển từ:
    * **shutdown phản ứng** sang
    * **derating chủ động và êm**.


### **7.3. Kết quả vận hành kỳ vọng**
Với kiến trúc AMOS–IKONOMY, các chỉ tiêu vận hành được cải thiện theo hướng:
  * **Uptime cao hơn** do giảm số lần dừng đột ngột.


  * **Tuổi thọ stack dài hơn** nhờ giảm sốc điện hóa và sốc nhiệt.


  * **Mức độ an toàn cao hơn** khi triển khai trong điều kiện hạ tầng và nhân lực hạn chế tại Việt Nam.


AMOS–IKONOMY không làm phần cứng mạnh hơn về lý thuyết, nhưng **làm cho phần cứng được sử dụng đúng giới hạn trong suốt vòng đời** , đây là yếu tố tạo khác biệt quyết định so với thiết kế IKONOMY ban đầu.
## **8\. Thông số kỹ thuật mục tiêu cho 01 mô-đun AMOS–IKONOMY**
Các thông số dưới đây là **giá trị thiết kế mục tiêu** , dùng làm cơ sở cho:
  * thiết kế phần cứng,


  * xây dựng thuật toán điều khiển AMOS,


  * thẩm định kỹ thuật và đánh giá vận hành.


### **8.1. Thông số điện – công suất**
|                           |
| **Thông số**              | **Giá trị thiết kế** | **Ghi chú kỹ thuật**                     |
|---------------------------|----------------------|------------------------------------------|
| Điện áp nguồn vào         | 48–96 VDC            | Dải cho phép, đã tính đến dao động nguồn |
| Công suất danh định       | 1,0 kW               | Vận hành liên tục dài hạn                |
| Công suất boost           | 1,5–2,0 kW           | Chỉ cho phép ngắn hạn, có điều kiện AMOS |
| Dòng làm việc danh định   | 20–25 A              | Xác định theo cấu hình stack             |
| Hiệu suất chuyển đổi điện | ≥ 95%                | Áp dụng cho khối Cannon Drive            |


**Ràng buộc vận hành:**
  * Công suất boost **không được xem là chế độ vận hành thường xuyên**.


  * Mọi trạng thái vượt công suất danh định đều chịu kiểm soát thời gian và điều kiện vật lý.


### **8.2. Thông số điện phân – hydro**
|                           |
| **Thông số**              | **Giá trị thiết kế** | **Ghi chú kỹ thuật**                  |
|---------------------------|----------------------|---------------------------------------|
| Sản lượng hydro danh định | ~300 L/giờ           | Tại dòng danh định, điều kiện ổn định |
| Hiệu suất Faraday         | 90–98%               | Phụ thuộc cấu hình stack              |
| Áp suất vận hành          | 1,5–3 bar            | Áp suất thấp, ưu tiên an toàn         |
| Lưu trữ H₂ khi dừng       | Không                | Thiết kế dừng an toàn, không tích khí |


**Nguyên tắc thiết kế:**
  * Sản lượng hydro được xác định trực tiếp bởi dòng điện.


  * Không sử dụng tích trữ hydro trong mô-đun để giảm rủi ro an toàn và áp lực cơ khí.


### **8.3. Thông số nhiệt – độ bền**
|                          |
| **Thông số**             | **Giá trị thiết kế** | **Ý nghĩa vận hành**                      |
|--------------------------|----------------------|-------------------------------------------|
| Nhiệt độ vận hành        | 55–75 °C             | Vùng tối ưu cho hiệu suất và độ bền       |
| Gradient nhiệt tối đa    | ≤ 5 °C               | Giới hạn bắt buộc để tránh ứng suất nhiệt |
| Tốc độ tăng nhiệt tối đa | ≤ 1 °C/phút          | Tránh sốc nhiệt và suy giảm nhanh         |
| Tuổi thọ mục tiêu        | 1,5–2× thiết kế gốc  | So với cùng cấu hình stack                |
| Uptime mục tiêu          | ≥ 98%                | Trong điều kiện vận hành thực tế          |


**Ràng buộc bắt b uộc:**
  * Khi vi phạm bất kỳ giới hạn nhiệt nào, hệ thống **bắt buộc giảm tải**.


  * Không cho phép duy trì công suất cao bằng cách chấp nhận vượt giới hạn nhiệt.


### **8.4. Nhận xét kỹ thuật tổng hợp**
  * Các thông số trên **không tối ưu cho công suất đỉnh** , mà tối ưu cho **vận hành ổn định dài hạn**.


  * Hiệu quả của AMOS–IKONOMY được đánh giá theo **hiệu suất vòng đời (lifetime performance)** , không theo giá trị tức thời.


  * Toàn bộ thuật toán AMOS được thiết kế để **bảo vệ các thông số này** , không cho phép vận hành ngoài phong bì đã định.


## **9\. Định nghĩa mặt bằng công nghệ hiện hành**
 _(Điện phân công suất nhỏ–trung bình)_
Trong bối cảnh hiện nay, **state-of-the-art (SOTA)** đối với hệ thống điện phân hydro công suất nhỏ–trung bình chủ yếu bao gồm các nhóm công nghệ sau:
  * **PEM electrolyzer thương mại** do các hãng EU, Mỹ và Nhật Bản phát triển.


  * **Alkaline electrolyzer thế hệ cải tiến** , tối ưu hiệu suất và độ ổn định so với thiết kế truyền thống.


  * **AEM electrolyzer thế hệ mới** , đang trong giai đoạn thương mại hóa sớm, độ ổn định dài hạn chưa được chứng minh đầy đủ.


### **9.1. Đặc trưng kỹ thuật chung của SOTA**
Các hệ thống SOTA hiện nay có các đặc điểm kỹ thuật chủ đạo sau:
  * Tối ưu hiệu suất điện năng tại **điều kiện vận hành chuẩn** , với nguồn điện ổn định và môi trường được kiểm soát.


  * Thiết kế giả định:
    * nguồn điện ít dao động,
    * có kỹ sư vận hành hoặc hệ thống giám sát chuyên sâu,
    * quy trình bảo trì được thực hiện đúng chuẩn nhà sản xuất.


  * Cơ chế bảo vệ chủ yếu dựa trên:
    * ngưỡng điện áp,
    * ngưỡng nhiệt,
    * và shutdown hoặc derating khi vượt ngưỡng.


Hạn chế chung của SOTA là **hiệu quả vận hành giảm đáng kể khi triển khai trong điều kiện thực tế biến động** , nơi các giả định về nguồn điện và nhân lực không còn đúng.
## **10\. So sánh trực tiếp AMOS–IKONOMY với IKONOMY ban đầu và SOTA**
### **10.1. Kiến trúc và triết lý điều khiển**
|                         |
| **Tiêu chí**            | **IKONOMY ban đầu**                          | **SOTA (PEM / Alkaline)**                  | **AMOS–IKONOMY**                         |
|-------------------------|----------------------------------------------|--------------------------------------------|------------------------------------------|
| Triết lý điều khiển     | Dựa nhiều vào phần cứng và thao tác vận hành | Điều khiển PID, derating theo ngưỡng chuẩn | Điều khiển theo dòng với phong bì vật lý |
| Biến điều khiển chính   | Dòng điện (chưa khóa cứng)                   | Công suất/điện áp theo cấu hình hệ         | Dòng điện (giới hạn cứng)                |
| Liên kết điện–nhiệt–khí | Yếu, xử lý rời rạc                           | Thường tách khối                           | Liên hợp, đồng thời                      |
| Khả năng vượt giới hạn  | Phụ thuộc người vận hành                     | Có thể xảy ra trước khi derating           | Không cho phép                           |


### **10.2. Công suất và sản lượng**
|                     |
| **Thông số**        | **IKONOMY ban đầu** | **SOTA**                         | **AMOS–IKONOMY**           |
|---------------------|---------------------|----------------------------------|----------------------------|
| Công suất danh định | ≈ 1 kW              | 1–5 kW/mô-đun (tùy nhà sản xuất) | 1 kW/mô-đun                |
| Chế độ boost        | Không xác định rõ   | Thường không khuyến nghị         | Có, kèm điều kiện bắt buộc |
| Sản lượng hydro     | 280–300 L/h         | 280–320 L/h                      | ≈ 300 L/h ổn định          |


AMOS–IKONOMY không nhắm tăng sản lượng danh định, mà **duy trì sản lượng gần trần vật lý trong thời gian dài**.
### **10.3. Tuổi thọ và suy giảm**
|                               |
| **Tiêu chí**                  | **IKONOMY ban đầu**     | **SOTA**                           | **AMOS–IKONOMY**                  |
|-------------------------------|-------------------------|------------------------------------|-----------------------------------|
| Phương thức theo dõi suy giảm | Thủ công hoặc gián tiếp | Theo lịch bảo trì, cảnh báo ngưỡng | Theo xu hướng thời gian thực      |
| Phát hiện suy giảm sớm        | Không hệ thống          | Hạn chế                            | Có (dR/dt, dT/dt, áp suất)        |
| Cơ chế phản ứng               | Cắt đột ngột            | Shutdown hoặc derating muộn        | Giảm tải sớm, có kiểm soát        |
| Tuổi thọ hữu dụng thực tế     | Phụ thuộc vận hành      | Cao nếu điều kiện chuẩn            | Cao hơn trong điều kiện biến động |


### **10.4. Vận hành và an toàn**
|                              |
| **Tiêu chí**                 | **IKONOMY ban đầu** | **SOTA**           | **AMOS–IKONOMY**           |
|------------------------------|---------------------|--------------------|----------------------------|
| Phụ thuộc con người          | Cao                 | Cao                | Thấp                       |
| Khả năng chịu dao động nguồn | Trung bình          | Thấp–trung bình    | Cao                        |
| Trạng thái khi dừng hệ thống | Có thể còn khí tồn  | Phụ thuộc thiết kế | Không lưu trữ khí khi dừng |
| Phản ứng khi lỗi             | Đột ngột            | Đột ngột           | Êm, có kiểm soát           |


### **10.5. Nhận xét tổng hợp**
  * **IKONOMY ban đầu** mạnh về phần cứng nhưng thiếu cơ chế khóa giới hạn ở cấp logic.


  * **SOTA hiện nay** đạt hiệu suất cao trong điều kiện chuẩn nhưng kém thích nghi với môi trường biến động.


  * **AMOS–IKONOMY** không vượt SOTA về hiệu suất phòng thí nghiệm, nhưng vượt trội về:
    * độ ổn định vận hành,
    * tuổi thọ hữu dụng,
    * an toàn triển khai thực tế.


AMOS–IKONOMY được thiết kế cho **điều kiện triển khai thật** , nơi các giả định của SOTA không còn đúng, và do đó đạt hiệu quả vòng đời cao hơn.
## **9\. Định nghĩa SOTA hiện nay (điện phân công suất nhỏ–trung bình)**
SOTA hiện nay chủ yếu gồm:
  * PEM electrolyzer thương mại (EU/Mỹ/Nhật),


  * Alkaline cải tiến,


  * AEM thế hệ mới (nhiều hệ còn chưa ổn định dài hạn).


Đặc trưng chung của SOTA:
  * tối ưu hiệu suất tại điều kiện chuẩn,


  * thiết kế cho môi trường vận hành được kiểm soát tốt,


  * phụ thuộc cao vào nguồn điện ổn định, quy trình bảo trì chuẩn, và kỹ sư vận hành.


## **10\. Bảng so sánh trực tiếp**
### **10.1. Kiến trúc và điều khiển**
|                         |
| **Tiêu chí**            | **IKONOMY ban đầu**                              | **SOTA (PEM / Alkaline)**                | **AMOS–IKONOMY**                                  |
|-------------------------|--------------------------------------------------|------------------------------------------|---------------------------------------------------|
| Triết lý điều khiển     | Tập trung phần cứng, phụ thuộc thao tác vận hành | PID và derating theo ngưỡng nhà sản xuất | Điều khiển theo dòng với phong bì vật lý bắt buộc |
| Biến điều khiển chính   | Dòng điện (chưa khóa cứng)                       | Công suất/điện áp theo cấu hình hệ       | Dòng điện (giới hạn cứng, không vượt)             |
| Liên kết điện–nhiệt–khí | Yếu, xử lý rời rạc                               | Phần lớn tách khối                       | Liên hợp, đánh giá đồng thời                      |
| Khả năng vượt giới hạn  | Có thể xảy ra do thao tác con người              | Có thể xảy ra trước khi derating         | Không cho phép trong mọi trạng thái               |


**Nhận xét kỹ thuật:** AMOS–IKONOMY chuyển quyền quyết định từ con người và phần cứng sang logic vật lý bắt buộc.
### **10.2. Công suất và sản lượng**
|                     |
| **Thông số**        | **IKONOMY ban đầu**      | **SOTA**                 | **AMOS–IKONOMY**                   |
|---------------------|--------------------------|--------------------------|------------------------------------|
| Công suất danh định | ≈ 1 kW                   | 1–5 kW/mô-đun (tùy hãng) | 1 kW/mô-đun                        |
| Chế độ boost        | Không định nghĩa rõ ràng | Thường không khuyến nghị | Có, nhưng bị khóa điều kiện vật lý |
| Sản lượng H₂        | ≈ 280–300 L/h            | 280–320 L/h              | ≈ 300 L/h ổn định dài hạn          |


**Nhận xét kỹ thuật:** AMOS–IKONOMY không nhắm tăng sản lượng đỉnh, mà duy trì sản lượng gần trần vật lý trong thời gian dài.
### **10.3. Tuổi thọ và suy giảm**
|                        |
| **Tiêu chí**           | **IKONOMY ban đầu**     | **SOTA**                           | **AMOS–IKONOMY**                       |
|------------------------|-------------------------|------------------------------------|----------------------------------------|
| Theo dõi suy giảm      | Thủ công hoặc gián tiếp | Theo lịch bảo trì, cảnh báo ngưỡng | Theo thời gian thực, dựa trên xu hướng |
| Phát hiện suy giảm sớm | Không hệ thống          | Hạn chế                            | Có (điện trở, nhiệt, áp suất)          |
| Cơ chế phản ứng        | Cắt đột ngột            | Shutdown hoặc derating muộn        | Giảm tải sớm, có kiểm soát             |
| Tuổi thọ hữu dụng      | Phụ thuộc vận hành      | Cao nếu điều kiện chuẩn            | Cao hơn trong điều kiện biến động      |


**Nhận xét kỹ thuật:** Lợi thế của AMOS–IKONOMY nằm ở quản lý suy giảm chủ động, không chờ đến ngưỡng hỏng.
### **10.4. Vận hành và an toàn**
|                              |
| **Tiêu chí**                 | **IKONOMY ban đầu** | **SOTA**           | **AMOS–IKONOMY**                  |
|------------------------------|---------------------|--------------------|-----------------------------------|
| Phụ thuộc con người          | Cao                 | Cao                | Thấp                              |
| Khả năng chịu dao động nguồn | Trung bình          | Thấp–trung bình    | Cao                               |
| Trạng thái khi dừng          | Có thể còn khí tồn  | Phụ thuộc thiết kế | Ưu tiên không lưu trữ H₂ khi dừng |
| Phản ứng khi lỗi             | Đột ngột            | Đột ngột           | Êm, giảm tải có kiểm soát         |


**Kết luận phần so sánh:** IKONOMY ban đầu mạnh về phần cứng nhưng thiếu khóa logic. SOTA mạnh trong điều kiện chuẩn nhưng kém thích nghi. AMOS–IKONOMY tối ưu cho vận hành thực tế biến động bằng cách khóa cứng giới hạn vật lý và tự động hóa quyết định bảo vệ, từ đó đạt hiệu quả vòng đời cao hơn.
## **11\. Phân tích nguyên nhân tạo ưu thế kỹ thuật**
### **11.1. So với thiết kế IKONOMY ban đầu**
Ưu thế của AMOS–IKONOMY so với IKONOMY ban đầu **không xuất phát từ phần cứng** , mà từ **cơ chế ra quyết định ở cấp hệ thống**.
Ba nguyên nhân kỹ thuật mang tính quyết định:
  1. **Giới hạn vật lý được tích hợp trực tiếp vào logic điều khiển**
Các giới hạn về dòng điện, nhiệt độ, gradient nhiệt, suy giảm điện hóa và áp suất khí được xem là ràng buộc bắt buộc trong mọi quyết định vận hành. Hệ thống không cho phép vượt phong bì vận hành đã xác định, ngay cả khi phần cứng còn dư khả năng chịu tải.


  2. **Loại bỏ khả năng cưỡng bức vận hành từ con người**
Quyền “ép chạy” do áp lực sản lượng hoặc đánh giá chủ quan bị loại bỏ khỏi chuỗi điều khiển. Người vận hành không thể buộc hệ thống vượt giới hạn thông qua thao tác thủ công.


  3. **Chuyển từ bảo vệ phản ứng sang bảo vệ phòng ngừa**
Thiết kế ban đầu chủ yếu dựa trên ngưỡng cắt khi sự cố đã hình thành.
AMOS–IKONOMY giám sát xu hướng suy giảm và giảm tải chủ động trước khi vượt ngưỡng nguy hiểm.


Hệ quả trực tiếp:
  * giảm sốc điện hóa và sốc nhiệt,


  * giảm dừng hệ thống đột ngột,


  * duy trì trạng thái vận hành ổn định trong thời gian dài hơn.


### **11.2. So với mặt bằng công nghệ SOTA hiện nay**
AMOS–IKONOMY **không cạnh tranh với SOTA ở hiệu suất phòng thí nghiệm**. Ưu thế của hệ thống thể hiện rõ khi triển khai trong **điều kiện vận hành thực tế có biến động** , nơi các giả định tiêu chuẩn của SOTA không còn hiệu lực.
Ba nguyên nhân chính:
  1. **Thiết kế chịu dao động nguồn**
Hệ thống không giả định nguồn điện ổn định. Logic điều khiển được xây dựng để duy trì an toàn và ổn định khi điện áp và công suất nguồn biến thiên.


  2. **Giảm yêu cầu nhân lực vận hành trình độ cao**
AMOS–IKONOMY không yêu cầu kỹ sư túc trực liên tục. Các quyết định bảo vệ chính được tự động hóa bằng luật vật lý cứng, không phụ thuộc phản ứng con người.


  3. **Tối ưu theo hiệu quả vòng đời**
Uptime, tuổi thọ stack và chi phí bảo trì được ưu tiên hơn hiệu suất đỉnh ngắn hạn. Điều này tạo lợi thế kinh tế rõ rệt trong vận hành dài hạn.


Trong điều kiện triển khai thực tế, AMOS–IKONOMY duy trì **hiệu quả sử dụng tổng thể cao hơn SOTA** , dù hiệu suất danh định tương đương.
## **12\. Kết luận kỹ thuật**
AMOS–IKONOMY **không nhằm vượt các định luật vật lý** , không thay đổi cơ chế điện phân nước và không theo đuổi các chỉ tiêu hiệu suất phòng thí nghiệm.
Giá trị kỹ thuật cốt lõi của hệ thống nằm ở việc **tổ chức và thực thi vận hành** theo các nguyên tắc sau:
  * **Chuyển các giới hạn vật lý, nhiệt và suy giảm vật liệu thành ràng buộc điều khiển bắt buộc** , được thực thi ở cấp logic trung tâm, không phụ thuộc vào quyết định vận hành.


  * **Giảm phụ thuộc vào con người** , loại bỏ khả năng cưỡng bức hệ thống vượt giới hạn do áp lực sản lượng hoặc đánh giá chủ quan.


  * **Duy trì vận hành ổn định gần giới hạn vật lý cho phép trong thời gian dài** , thay vì tối ưu công suất đỉnh ngắn hạn dẫn đến suy giảm nhanh.


So với thiết kế IKONOMY ban đầu và mặt bằng công nghệ điện phân hiện hành, AMOS–IKONOMY đạt **hiệu quả sử dụng thực tế cao hơn trên toàn bộ vòng đời** , đặc biệt phù hợp với điều kiện triển khai tại Việt Nam và các môi trường có đặc tính vận hành tương đương.
* * *
# **KIẾN TRÚC TỔNG THỂ & CHI PHÍ HỆ THỐNG AMOS–IKONOMY (01 MÔ-ĐUN ~1 kW)**
* * *
## **I. KIẾN TRÚC TỔNG THỂ (ARCHITECTURE CHART)**
### **1\. Chuỗi chức năng bắt buộc**
|         |
| **STT** | **Khối**                 | **Đầu vào** | **Đầu ra**        | **Chức năng kỹ thuật**      |
|---------|--------------------------|-------------|-------------------|-----------------------------|
| 1       | Nguồn DC                 | 48–96 VDC   | DC thô            | Cấp năng lượng              |
| 2       | Điều hòa & bảo vệ        | DC thô      | DC sạch           | Chống xung, đảo cực, inrush |
| 3       | Cannon (điều khiển dòng) | DC sạch     | Dòng DC định hình | Điều khiển dòng theo AMOS   |
| 4       | Stack điện phân          | Dòng DC     | H₂ + nhiệt        | Tạo hydro                   |
| 5       | Quản lý nhiệt            | Nhiệt       | Nhiệt ổn định     | Giới hạn dT/dt, ΔT          |
| 6       | Tách & điều hòa khí      | H₂ thô      | H₂ ổn định        | Ổn định áp, an toàn         |
| 7       | Ngõ ra H₂                | H₂          | H₂ sử dụng        | Không lưu trữ khi dừng      |


**Nguyên tắc:** Không có quyết định công suất nào đi thẳng từ “nhu cầu H₂” xuống stack. Mọi thay đổi dòng phải qua Cannon và bị khóa bởi AMOS.
* * *
### **2\. Phân quyền quyết định**
|                |
| **Thực thể**   | **Tăng dòng** | **Giảm dòng**  | **Ghi chú**            |
|----------------|---------------|----------------|------------------------|
| Người vận hành | Không         | Không          | Không có quyền ép chạy |
| Cannon         | Không         | Có (theo lệnh) | Chỉ thực thi           |
| AMOS           | Có            | Có             | Bị ràng buộc vật lý    |
| Stack          | Không         | Không          | Thụ động               |


* * *
## **II. CẤU TRÚC THEO KHỐI (TECH BLOCK CHART)**
### **3\. Khối nguồn & bảo vệ**
|              |
| **Hạng mục** | **Mục tiêu**     | **Cách kiểm chứng**   |
|--------------|------------------|-----------------------|
| Dải điện áp  | 48–96 VDC (±15%) | Test brown-out/ripple |
| Inrush       | ≤ 1,5×I_nom      | Đo clamp ≥10 kHz      |
| Bảo vệ       | TVS, LC, đảo cực | Test xung/đảo cực     |


* * *
### **4\. Khối Cannon (Power + Control)**
|              |
| **Hạng mục** | **Mục tiêu**                    |
|--------------|---------------------------------|
| Topology     | Buck/Buck–Boost đồng bộ         |
| Điều khiển   | Vòng kín theo dòng              |
| Dải dòng     | 1–20 A (rated); 25–30 A (boost) |
| Giới hạn     | dI/dt ≤ 0,5 A/ms                |
| Hiệu suất    | 94–97%                          |
| Đo dòng      | Sai số ≤ 1%                     |


* * *
### **5\. Stack điện phân**
|             |
| **Tham số** | **Giá trị mục tiêu**   |
|-------------|------------------------|
| Công suất   | 1,0 kW danh định       |
| Dòng        | 20–25 A                |
| Điện áp     | 40–60 V                |
| Vùng chạy   | Ổn định + boost ngắn   |
| Giới hạn    | Tafel, nhiệt, suy giảm |


* * *
### **6\. Quản lý nhiệt**
|             |
| **Tham số** | **Ngưỡng**                 |
|-------------|----------------------------|
| Nhiệt độ    | 55–75 °C                   |
| dT/dt       | ≤ 1 °C/phút                |
| ΔT stack    | ≤ 5 °C                     |
| Chiến lược  | Giảm dòng trước, không cắt |


* * *
### **7\. Nước & khí**
|                 |
| **Thành phần**  | **Mục tiêu**     |
|-----------------|------------------|
| Áp suất         | 1,5–3 bar        |
| Ripple áp       | ≤ 3% RMS         |
| Carry-over nước | 0 (thiết kế)     |
| Dừng máy        | Không lưu trữ H₂ |


* * *
## **III. CHI PHÍ CHI TIẾT (COST BREAKDOWN)**
### **8\. Chi phí phần cứng theo khối (USD/mô-đun)**
|         |
| **STT** | **Khối**                 | **Thấp** | **Cao** |
|---------|--------------------------|----------|---------|
| 1       | Nguồn & bảo vệ           | 40       | 55      |
| 2       | Cannon (công suất + MCU) | 80       | 120     |
| 3       | Stack điện phân          | 230      | 390     |
| 4       | Hệ thống nhiệt           | 50       | 80      |
| 5       | Nước & khí               | 40       | 70      |
| 6       | Khung + dây + lắp        | 30       | 50      |
| **—**   | **Tổng**                 | **470**  | **760** |


* * *
### **9\. Tỷ trọng chi phí**
|            |
| **Khối**   | **Tỷ trọng** |
|------------|--------------|
| Stack      | 45–55%       |
| Cannon     | 15–20%       |
| Nhiệt      | 8–10%        |
| Nước & khí | 8–10%        |
| Khác       | 10–15%       |


* * *
### **10\. Chi phí theo quy mô sản xuất**
|             |
| **Quy mô**  | **USD/mô-đun** | **Ghi chú**  |
|-------------|----------------|--------------|
| 50–100/năm  | 650–800        | Lắp thủ công |
| 300–500/năm | 520–650        | Chuẩn hóa    |
| ~1.000/năm  | 450–600        | Mua số lượng |


* * *
## **IV. GIÁ TRỊ VÒNG ĐỜI (LIFETIME VALUE)**
### **11\. So sánh vận hành**
|                  |
| **Chỉ tiêu**     | **Hệ thường** | **AMOS–IKONOMY** |
|------------------|---------------|------------------|
| Uptime mục tiêu  | 90–95%        | ≥ 98%            |
| Tuổi thọ stack   | Chuẩn         | +50–100%         |
| Dừng đột ngột    | Có            | Rất thấp         |
| Chi phí vòng đời | Cao           | Thấp hơn 25–40%  |


## **KẾT LUẬN VỀ CHI PHÍ HỆ THỐNG AMOS–IKONOMY**
  1. **Chi phí đầu tư ban đầu (CAPEX) ở mức trung bình–thấp trong phân khúc**


  * Chi phí p hần cứng cho 01 mô-đun ~1 kW nằm trong khoảng **470–760 USD** ở quy mô nhỏ.


  * Khi sản xuất 300–1.000 mô-đun/năm, chi phí có thể giảm về **450–600 USD/mô-đun** nhờ chuẩn hóa và mua linh kiện số lượng.


  * Mức này **thấp hơn rõ rệt** so với mô-đun điện phân nhập khẩu cùng công suất, vốn thường cao hơn do chi phí stack, logistics và phụ thuộc nhà cung cấp.


**Cấu trúc chi phí hợp lý, không “đội giá” ở phần điều khiển**
  * Stack điện phân chiếm **45–55% tổng chi phí** , đúng với mặt bằng kỹ thuật chung.


  * Phần điều khiển Cannon + AMOS chỉ chiếm **15–20%** , nhưng tạo ra giá trị lớn nhất về tuổi thọ và độ ổn định.


  * Không phát sinh chi phí cho phần cứng phức tạp hoặc vật liệu đặc biệt khó nội địa hóa.


**Chi phí vận hành (OPEX) thấp nhờ logic giảm tải sớm**
  * AMOS giảm số lần dừng đột ngột và sự cố ngoài kế hoạch.


  * Tuổi thọ stack tăng **50–100%** , kéo dài chu kỳ thay thế.


  * Nhu cầu kỹ sư túc trực thấp, giảm chi phí nhân sự vận hành.


**Chi phí vòng đời (LCOH) thấp hơn dù CAPEX không tối thiểu**
  * AMOS–IKONOMY không tối ưu để rẻ nhất lúc mua, mà tối ưu để **rẻ nhất trong suốt vòng đời**.


  * Với uptime mục tiêu ≥ 98% và suy giảm được kiểm soát, **chi phí hydro/kg trong vòng đời giảm 25–40%** so với hệ thống vận hành theo ngưỡng cắt thông thường.


  * Lợi thế này càng rõ trong điều kiện nguồn điện dao động và môi trường khó kiểm soát.


**Phù hợp nội địa hóa và mở rộng quy mô tại Việt Nam**
  * Tỷ lệ nội địa hóa phần cơ khí, nhiệt, lắp ráp đạt **60–70%**.


  * Không phụ thuộc chuỗi cung ứng phức tạp.


  * Mô hình chi phí tuyến tính theo số mô-đun, phù hợp triển khai phân tán (đảo, cảng, khu công nghiệp).


Về chi phí, AMOS–IKONOMY đạt **điểm cân bằng tối ưu** giữa CAPEX, OPEX và rủi ro vận hành. Hệ thống **không rẻ nhất khi mua** , nhưng **rẻ nhất khi vận hành dài hạn** , đặc biệt trong điều kiện thực tế tại Việt Nam.
# **TẬP PHƯƠNG TRÌNH CỐT LÕI CỦA HỆ THỐNG AMOS–IKONOMY**
* * *
## **I. Cơ sở vật lý bắt buộc của điện phân nước**
### **1\. Quan hệ giữa dòng điện và sản lượng hydro (Luật Faraday)**
1.1. Sản lượng hydro sinh ra tỉ lệ tuyến tính với dòng điện chạy qua stack.
1.2. Điện áp không quyết định lượng hydro tạo thành.
1.3. Không thể tăng sản lượng nếu không tăng dòng điện.
1.4. Phương trình:
  * Lưu lượng H₂ (mol/s) = (η_F × I) / (2 × F)


  * Viết dạng số: Lưu lượng H₂ (mol/s) = (η_F × I) / 192970


1.5. Biến số:
  * I: dòng điện qua stack, dải 10–30 A.


  * η_F: hiệu suất Faraday, dải 0,90–0,98.


  * F: hằng số Faraday, 96485 C/mol.


1.6. Áp dụng trong AMOS:
  * Dòng điện là biến điều khiển duy nhất.


  * Điện áp không được dùng để điều khiển công suất.


* * *
### **2\. Quy đổi sang lưu lượng thể tích (phục vụ thiết kế)**
2.1. Ở điều kiện tiêu chuẩn, 1 mol H₂ ≈ 22,4 L.
2.2. Công thức thực dụng:
  * Lưu lượng H₂ (L/h) ≈ 0,418 × I × η_F.


2.3. Ví dụ:
  * I = 25 A.


  * η_F = 0,95.


  * Lưu lượng ≈ 9,9 L/h.


2.4. Ý nghĩa thiết kế:
  * Công suất và sản lượng module được xác định trực tiếp từ dòng điện thiết kế.


  * Không tồn tại hệ số tối ưu vượt phương trình này.


* * *
## **II. Phương trình điện áp stack (chỉ dùng giám sát)**
### **3\. Phân rã điện áp stack**
3.1. Biểu thức tổng quát:
  * V_stack = E_rev(T)
\+ η_hoạt_hóa(I,T)
\+ I × R_tương_đương(T)
\+ η_truyền_khối(I).


3.2. Ý nghĩa thành phần:
  * E_rev: điện áp thuận nghịch, phụ thuộc nhiệt độ.


  * η_hoạt_hóa: tổn hao động học phản ứng.


  * I × R: tổn hao điện trở.


  * η_truyền_khối: tổn hao khuếch tán và bọt khí.


3.3. Nguyên tắc sử dụng trong AMOS:
  * Không dùng điện áp để ép dòng.


  * Chỉ dùng để giám sát trạng thái.


  * Chỉ dùng để phát hiện suy giảm và bất thường vận hành.


* * *
## **III. Phương trình suy giảm – lõi khác biệt của AMOS**
### **4\. Điện trở tương đương của stack**
4.1. Định nghĩa:
  * R_eq(t) = [V_stack(t) − E_rev(T)] / I(t).


4.2. AMOS không sử dụng giá trị tức thời.
4.3. AMOS theo dõi xu hướng thay đổi theo thời gian.
* * *
### **5\. Tốc độ suy giảm điện trở**
5.1. Chỉ số giám sát chính:
  * dR/dt = ΔR / Δt.


5.2. Diễn giải vận hành:
  * dR/dt ≈ 0: stack ổn định.


  * dR/dt tăng chậm: lão hóa bình thường.


  * dR/dt tăng nhanh: suy giảm không hồi phục.


5.3. Luật điều khiển cứng:
  * dR/dt vượt ngưỡng → cấm tăng dòng.


  * dR/dt tiếp tục tăng → giảm dòng chủ động.


5.4. AMOS không chờ hỏng mới phản ứng.
* * *
## **IV. Tránh vùng Tafel dốc (vùng phá tuổi thọ)**
### **6\. Quan hệ Tafel (xấp xỉ)**
6.1. Biểu thức:
  * η_hoạt_hóa ≈ a + b × log(I).


6.2. Khi dòng vượt ngưỡng:
  * Tổn hao tăng phi tuyến.


  * Suy giảm vật liệu tăng mạnh.


6.3. Định nghĩa vùng cấm:
  * I > I_Tafel.


  * Chỉ cho phép trong thời gian ngắn.


  * Bắt buộc có giai đoạn hồi phục.


6.4. Luật AMOS:
  * Boost trên I_Tafel bị giới hạn thời gian.


  * Không cho phép boost lặp dày.


* * *
## **V. Phương trình nhiệt – giới hạn sống còn**
### **7\. Cân bằng nhiệt đơn giản hóa**
7.1. Biểu thức điều khiển:
  * C_nhiệt × (dT/dt)
= P_điện − P_phản_ứng − hA(T − T_môi_trường).


7.2. Biến số:
  * C_nhiệt: nhiệt dung hiệu dụng.


  * dT/dt: tốc độ tăng nhiệt.


  * P_điện: công suất điện vào.


  * P_phản_ứng: công suất tạo H₂.


  * hA: khả năng tản nhiệt.


* * *
### **8\. Giới hạn nhiệt bắt buộc**
8.1. Giới hạn cứng:
  * dT/dt ≤ 1 °C/phút.


  * ΔT_stack ≤ 5 °C.


8.2. Luật điều khiển:
  * Vi phạm bất kỳ giới hạn nào → giảm dòng ngay.


  * Không chờ cảnh báo.


  * Không cắt đột ngột, trừ trường hợp an toàn tuyệt đối.


* * *
## **VI. Luật tổng hợp ra quyết định của AMOS**
9.1. AMOS chỉ cho phép tăng dòng khi đồng thời thỏa mãn:
  * dR/dt thấp.


  * Nhiệt độ và gradient ổn định.


  * Áp suất khí ổn định.


  * Không có stress tích lũy gần đây.


9.2. Nguyên tắc quyết định:
  * Nếu tăng sản lượng ngắn hạn nhưng làm tăng xác suất hỏng trong tương lai → hành động bị từ chối.


* * *
## **Kết luận kỹ thuật**
10.1. AMOS–IKONOMY không vượt định luật vật lý.
10.2. AMOS–IKONOMY không thay đổi hóa học.
10.3. AMOS–IKONOMY không phá Luật Faraday.
10.4. Khác biệt cốt lõi:
  * Chuyển các phương trình vật lý thành luật điều khiển bắt buộc.


  * Không phụ thuộc giám sát thủ công của con người.


10.5. Hệ quả trực tiếp:
  * Tuổi thọ hệ thống dài hơn.


  * Mức độ an toàn cao hơn.


  * Chi phí vòng đời thấp hơn.


# **Sơ đồ khối tổng thể**
```
    [NGUỒN DC 48–96V]
       |
       v
    [KHỐI BẢO VỆ & ĐIỀU HÒA NGUỒN]
    (OVP/UVP, đảo cực, hạn dòng khởi động, TVS, lọc LC)
       |
       v
    [LỌC EMI/EMC & PHÂN VÙNG NỐI ĐẤT]
    (tách mass công suất / mass tín hiệu / chassis)
       |
       v
    [KHỐI CÔNG SUẤT CANNON]
    (buck hoặc buck-boost đồng bộ, điều khiển theo DÒNG)
       |--------------------\
       |                     \
       v                      v
    [ĐO DÒNG]              [ĐO ÁP STACK]
    (shunt/Hall + ADC)     (tổng + tuỳ chọn chia đoạn)
       \                     /
        \                   /
         v                 v
    [MCU THỜI GIAN THỰC]
    (vòng điều khiển dòng 0,1–1 kHz,
    giới hạn dI/dt, tạo thư viện dạng sóng)
         |
         v
    [STACK ĐIỆN PHÂN]
         |
         +--> [PHẦN CỨNG NHIỆT] --> [CẢM BIẾN NHIỆT T1..T3]
         |
         +--> [TÁCH KHÍ H2/O2] --> [BẪY NƯỚC / BUBBLER / LỌC]
         |                          |
         |                          v
         |                      [VAN/ĐIỀU ÁP H2] --> [NGÕ RA H2]
         |
         +--> [HỆ NƯỚC] --> [CẢM BIẾN MỨC] + [CẢM BIẾN ĐỘ DẪN (tuỳ chọn)]
         |
         +--> [CẢM BIẾN ÁP SUẤT P + DAO ĐỘNG ÁP]
    
    [AMOS CORE]
    (ước lượng trạng thái, tích luỹ suy giảm, quản lý phong bì,
    logic cấp/khóa boost, chính sách giảm tải)
         |
         v
    [GIÁM SÁT / KIỂM TOÁN]
    (log, truy vết quyết định, báo cáo uptime, can thiệp, trend suy giảm)
```
* * *
# **1) Bảng tín hiệu I/O (đủ để viết firmware + thiết kế mạch đo)**
> Gợi ý đọc: “Tần số lấy mẫu” là **tốc độ MCU đọc và xử lý**. Một số tín hiệu đo nhanh nhưng chỉ cần **lọc và downsample** cho AMOS.
|                           |
| **Tên tín hiệu**          | **Loại cảm biến/nguồn**   | **Kiểu tín hiệu** | **Tần số lấy mẫu (khuyến nghị)**  | **Độ chính xác mục tiêu** | **Mục đích điều khiển**                       | **Nếu lỗi tín hiệu (fail-safe)**    |
|---------------------------|---------------------------|-------------------|-----------------------------------|---------------------------|-----------------------------------------------|-------------------------------------|
| VBUS_IN                   | Chia áp + ADC             | Analog            | 100–500 Hz                        | ±2%                       | phát hiện sụt áp/dao động nguồn, feed-forward | giới hạn công suất, cấm boost       |
| I_STACK                   | Shunt + INA / Hall + ADC  | Analog            | 1–5 kHz (vòng dòng), log 10–50 Hz | ≤±1%                      | điều khiển dòng vòng kín, tính Faraday        | clamp dòng về 0, vào Protective     |
| V_STACK_TOTAL             | Chia áp + ADC             | Analog            | 500–1.000 Hz, log 10–50 Hz        | ≤±1%                      | tính R_eq, phát hiện bất thường điện hoá      | cấm boost, derate                   |
| V_STACK_SEG[i] (tuỳ chọn) | Chia áp nhiều kênh        | Analog            | 100–500 Hz                        | ≤±1.5%                    | phát hiện lệch cục bộ (hotspot điện hoá)      | derate, báo bảo trì                 |
| T1 (inlet/plate)          | NTC/PT1000                | Analog            | 10–50 Hz                          | ±0.5°C                    | kiểm soát dT/dt                               | kết thúc boost, derate              |
| T2 (core/hotspot)         | NTC/PT1000                | Analog            | 10–50 Hz                          | ±0.5°C                    | kiểm soát T_max, ΔT                           | Protective nếu vượt hard            |
| T3 (outlet/case)          | NTC/PT1000                | Analog            | 10–50 Hz                          | ±0.5°C                    | đánh giá gradient và tản nhiệt                | cấm boost                           |
| P_H2                      | Cảm biến áp suất          | Analog            | 10–50 Hz                          | ±1% FS                    | kiểm soát áp, phát hiện surge                 | derate, Protective nếu vượt hard    |
| P_RIPPLE (tính toán)      | từ P_H2                   | số                | 10–50 Hz                          | —                         | cấm boost khi dao động áp cao                 | cấm boost, derate                   |
| WL (mức nước)             | phao/siêu âm/cảm biến mức | Digital/Analog    | 1–5 Hz                            | ±5% mức                   | cấm boost khi thiếu nước                      | Degraded hoặc shutdown có kiểm soát |
| COND (tuỳ chọn)           | cảm biến độ dẫn           | Analog            | 0,2–1 Hz                          | ±5–10%                    | đánh giá chất lượng nước, derate theo bậc     | Degraded, yêu cầu thay nước         |
| H2_LEAK (khuyến nghị)     | cảm biến H2               | Digital/Analog    | 1–10 Hz                           | theo ISO/IEC              | an toàn rò rỉ                                 | Safety trip độc lập                 |
| DOOR/INTERLOCK            | công tắc                  | Digital           | 10–100 Hz                         | —                         | liên động an toàn                             | Safety trip                         |
| FAN_PUMP_FB               | tach/feedback             | Digital           | 10–50 Hz                          | —                         | xác nhận làm mát hoạt động                    | cấm boost, derate                   |
| E_STOP                    | nút dừng khẩn             | Digital           | 100 Hz                            | —                         | cắt an toàn                                   | cắt enable lập tức                  |


* * *
# **2) Bảng ngưỡng vận hành (Cruise / Boost / Degraded) + phản ứng hệ thống**
> Lưu ý quan trọng để “đứng hồ sơ”: các số dưới đây là **giá trị cấu hình mục tiêu** (design targets) cho mô-đun ~1 kW. Khi chốt hoá học (PEM/AEM/kiềm) và dữ liệu chạy dài hạn, bạn sẽ **điều chỉnh dải**.
## **2.1 Ngưỡng nhiệt**
|                           |
| **Tham số**               | **Cruise**                     | **Boost (được phép)**          | **Degraded** | **Phản ứng hệ thống**                                   |
|---------------------------|--------------------------------|--------------------------------|--------------|---------------------------------------------------------|
| Nhiệt độ trung bình T_avg | 58–65°C                        | chỉ khi T_avg ≤ (T_soft − 2°C) | 50–60°C      | vượt T_soft → derate theo bậc; vượt T_hard → Protective |
| Nhiệt độ cực đại T_max    | T_hard = 72–78°C (tuỳ profile) | cấm nếu gần T_hard             | —            | T ≥ T_hard → ramp-down + lockout nếu lặp                |
| Gradient nhiệt ΔT         | ≤3–5°C                         | phải ≤ (ΔT_soft − margin)      | ≤2–4°C       | ΔT vượt soft → cấm boost; vượt hard → Protective        |
| Tốc độ tăng nhiệt dT/dt   | ≤0,6–1,0°C/phút                | chỉ khi dT/dt thấp             | ≤0,5°C/phút  | dT/dt cao → kết thúc boost + cooldown                   |


## **2.2 Ngưỡng điện – công suất**
|                 |
| **Tham số**     | **Cruise**    | **Boost**                | **Degraded** | **Phản ứng hệ thống**                   |
|-----------------|---------------|--------------------------|--------------|-----------------------------------------|
| Công suất P_in  | 0,8–1,0 kW    | 1,2–2,0 kW (tuỳ profile) | 0,3–0,8 kW   | boost chỉ theo “ngân sách” và điều kiện |
| Dòng I_stack    | 8–15 A        | 18–30 A                  | 3–12 A       | hard clamp khi vượt I_hard              |
| Giới hạn dI/dt  | ≤0,3–0,6 A/ms | bắt buộc                 | bắt buộc     | vượt → gate driver/MCU không cho phép   |
| Ripple dòng RMS | ≤1–3%         | ≤2–4%                    | ≤2%          | ripple cao → đổi dạng sóng / giảm I     |


## **2.3 Ngưỡng khí**
|                         |
| **Tham số**             | **Cruise**            | **Boost**              | **Degraded** | **Phản ứng hệ thống**                          |
|-------------------------|-----------------------|------------------------|--------------|------------------------------------------------|
| Áp suất P_H2            | 1,2–3,0 bar           | chỉ khi P còn headroom | 1,0–2,5 bar  | vượt P_soft → derate; vượt P_hard → Protective |
| Ripple áp suất P_ripple | ≤2–3%                 | ≤2–3%                  | ≤2%          | ripple cao → cấm boost + giảm dòng             |
| dP/dt                   | giới hạn theo profile | chặt hơn               | chặt         | surge → giảm dòng ngay                         |


## **2.4 Ngưỡng nước**
|                        |
| **Tham số**            | **Cruise** | **Boost**           | **Degraded**  | **Phản ứng hệ thống**                                        |
|------------------------|------------|---------------------|---------------|--------------------------------------------------------------|
| Mức nước WL            | ≥35–40%    | ≥55–60%             | ≥25–35%       | WL thấp → cấm boost, derate; WL_crit → shutdown có kiểm soát |
| Độ dẫn COND (tuỳ chọn) | theo band  | phải tốt hơn Cruise | band rộng hơn | vượt → giảm theo bậc + yêu cầu bảo trì                       |


## **2.5 Ngân sách Boost (điểm “khác biệt” để bảo vệ tuổi thọ)**
|                       |
| **Chỉ tiêu**          | **Lab**  | **Công nghiệp** | **Hàng hải-đảo** | **Phản ứng hệ thống**                |
|-----------------------|----------|-----------------|------------------|--------------------------------------|
| t_boost_max (mỗi lần) | 180 s    | 120 s           | 60–90 s          | hết thời gian → bắt buộc cooldown    |
| cooldown tối thiểu    | 3–5 phút | 5–10 phút       | 10–15 phút       | trong cooldown: cấm boost            |
| số lần boost/giờ      | 6        | 3               | 1–2              | vượt → cấm boost                     |
| tổng boost/ngày       | 30 phút  | 10–15 phút      | 5–8 phút         | vượt → cấm boost đến hết ngày        |
| số lỗi trước lockout  | 3        | 2               | 1–2              | lặp lỗi → Lockout + yêu cầu kiểm tra |


* * *
# **3) Bảng log và truy vết kiểm toán (audit-ready)**
Mục tiêu của bảng này là: **mỗi quyết định quan trọng đều có “vì sao” + “dữ liệu nào” + “ai/phiên bản nào”**. Đây là thứ hội đồng/đăng kiểm yêu cầu khi bạn nói “hệ tự từ chối boost”.
|                                                        |
| **Sự kiện/Quyết định**                                 | **Bắt buộc lưu trường dữ liệu**                                                                                                 | **Tần suất**                | **Vì sao hội đồng cần**                    | **Thời gian lưu** |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------|-------------------|
| Chuyển mode (Cruise/Boost/Degraded/Protective/Lockout) | timestamp; mode_from; mode_to; reason_code; snapshot(T_avg, ΔT, dT/dt, P, P_ripple, I, V, R_eq, dR/dt, WL, Cond); firmware_hash | mỗi lần                     | chứng minh quyết định có căn cứ đo được    | ≥12–24 tháng      |
| Cấp Boost / Từ chối Boost                              | boost_request_id; decision(allow/deny); violated_conditions list; margins; boost_budget_remaining; cooldown_state               | mỗi lần                     | chứng minh “refusal logic”                 | ≥12–24 tháng      |
| Trip/Protective                                        | trip_type; sensor_causing; threshold; pre-trip trace 10–30 s (I,V,T,P); recovery sequence                                       | mỗi lần                     | chứng minh an toàn và điều tra nguyên nhân | ≥24 tháng         |
| Derate theo bậc                                        | derate_level; active_constraints; commanded_I; actual_I; duration                                                               | 1–5 Hz log gọn              | chứng minh giảm tải êm, không “cắt sốc”    | ≥6–12 tháng       |
| Drift/suy giảm                                         | R_eq trend; dR/dt; D_index (nếu dùng); health_state                                                                             | 1 lần/giờ + khi vượt ngưỡng | chứng minh kiểm soát tuổi thọ              | ≥24 tháng         |
| Thay đổi cấu hình ngưỡng                               | param_name; old/new; user_role; auth_method; reason; ticket_id                                                                  | mỗi lần                     | chống “tinh chỉnh lén” để đẹp số           | ≥24 tháng         |
| Cập nhật firmware                                      | version; hash; signed_by; rollback_protect; change_log                                                                          | mỗi lần                     | traceability theo IEC 61508/62443          | ≥24 tháng         |
| Mất cảm biến / plausibility fail                       | sensor_id; fail_mode; fallback_action                                                                                           | mỗi lần                     | chứng minh fail-safe                       | ≥24 tháng         |


**Quy ước reason_code (bắt buộc chuẩn hoá):**
Ví dụ: DENY_BOOST_T_GRADIENT, DERATE_P_RIPPLE, LOCKOUT_REPEAT_TRIP, … để đọc log là hiểu ngay.
* * *
# **4) “Mô tả mạch power stage” đủ để giao thiết kế PCB (mức khối + ràng buộc layout)**
## **4.1 Khối đầu vào (Front-End)**
**Mục tiêu:** bảo vệ bus, giảm nhiễu, không cho “đột biến nguồn” đánh vào stack.
  * Bảo vệ đảo cực: MOSFET “ideal diode” (ưu tiên) hoặc diode + cầu chì


  * Hạn dòng khởi động: mạch soft-start (MOSFET + driver) hoặc NTC (nếu chấp nhận tổn hao)


  * TVS: chọn theo bus 48/96V và kịch bản surge (tính công suất xung)


  * Lọc EMI đầu vào: cấu hình π (C–L–C) với tụ film đặt sát vòng dòng lớn


**Ràng buộc layout bắt buộc:**
  * vòng dòng công suất (MOSFET-inductor-cap) phải **ngắn nhất có thể**


  * mass công suất và mass tín hiệu phải tách, chỉ nối tại **một điểm sao**


  * đặt vị trí dự phòng snubber/RC để tinh chỉnh khi test EMC


## **4.2 Topology công suất**
**Lựa chọn topology:**
  * Nếu điện áp stack luôn thấp hơn bus: **buck đồng bộ**


  * Nếu điện áp stack có thể gần/vượt bus theo cấu hình: **buck-boost 4 công tắc**


**Khối chính:**
  * MOSFET công suất (2 cái cho buck; 4 cái cho buck-boost)


  * Gate driver có:
    * điều khiển dead-time
    * điều khiển tốc độ cạnh (slew-rate) để kìm dI/dt và EMI
    * UVLO + fault flag


  * Inductor công suất: dòng bão hoà phải > I_boost + biên ripple


  * Tụ đầu ra: phối hợp điện phân low-ESR + film để dập xung nhanh


  * Snubber RC/RCD: giảm ringing và stress MOSFET


**Chỉ tiêu thiết kế nên ghi trong yêu cầu PCB:**
  * hiệu suất khối công suất: ≥94% ở Cruise, ≥92% ở Boost


  * nhiệt độ junction MOSFET ở Boost: không vượt giới hạn thiết kế (cần mô phỏng nhiệt + heatsink/thermal pad)


  * ripple dòng RMS: theo profile (thường 1–3% Cruise)


## **4.3 Đo dòng (phần “không được sai”)**
  * Phương án A (ưu tiên điều khiển chính xác): **shunt mΩ + khuếch đại đo dòng + ADC**


  * Phương án B (cách ly, dễ triển khai): **Hall-effect**


**Ràng buộc:** băng thông đo phải đủ cho vòng dòng (ít nhất vài kHz), có lọc analog chống aliasing.
* * *
# **5) So sánh định lượng: IKONOMY nguyên bản vs AMOS-IKONOMY vs SOTA (viết kiểu “không bị bắt bẻ”)**
Bạn chỉ được phép viết theo 2 lớp: **(i) số đã đo** , **(ii) mục tiêu thiết kế kèm kế hoạch chứng minh**.
## **5.1 KPI vận hành (cái SOTA hay yếu)**
|                          |
| **Chỉ tiêu**             | **IKONOMY nguyên bản (chưa có AMOS)** | **AMOS-IKONOMY (mục tiêu thiết kế)** | **SOTA thương mại (điển hình)**  |
|--------------------------|---------------------------------------|--------------------------------------|----------------------------------|
| Uptime                   | 90–94% (thường dao động)              | ≥98%                                 | 92–97% (tuỳ hệ, tuỳ môi trường)  |
| Trip/1000 giờ            | 5–15                                  | ≤1–3                                 | 2–10                             |
| MTBC (giờ)               | 100–300                               | 500–1500                             | 200–800                          |
| Can thiệp/tuần           | 2–10                                  | ≤1                                   | 1–5                              |
| Boost “an toàn có audit” | thường không chuẩn hoá                | có (ngân sách + log)                 | thường không có / không cho phép |


> Lưu ý: “SOTA điển hình” biến thiên rất lớn theo hãng và ứng dụng. Khi nộp hồ sơ, bạn nên ghi “khoảng tham chiếu thị trường” và kèm test plan của mình.
## **5.2. LCOH proxy (chỉ số so sánh nhanh, không thay thế LCA đầy đủ)**
Để so sánh các phương án thiết kế và vận hành **khi chưa có phân tích vòng đời (LCA) hoàn chỉnh** , sử dụng chỉ số **LCOH proxy** với công thức đã được chuẩn hóa, dễ hiểu và dễ kiểm toán.
### **Định nghĩa sản lượng hiệu dụng**
$$Q_{eff}=Q_{H2}\cdot U$$
Trong đó:
  * $Q_{H2}$: sản lượng hydro danh định theo giờ (đo thực tế, tại điều kiện chuẩn đã khai báo).


  * $U$: uptime vận hành (tỷ lệ thời gian hệ thống tạo hydro hợp lệ).


### **Công thức LCOH proxy**
$$LCOH_{proxy}=\frac{C_{elec,h}+C_{cap,h}+C_{maint,h}}{Q_{eff}}$$
Với các thành phần chi phí:
  * $C_{elec,h}=P_{in}\cdot c_{kWh}$
(chi phí điện theo giờ, từ công suất điện vào và giá điện)


  * $C_{cap,h}=\frac{CAPEX}{Life_h}$
(chi phí khấu hao theo giờ, dựa trên tuổi thọ hữu dụng thực tế)


  * $C_{maint,h}=\frac{OPEX_{year}}{8760}$
(chi phí vận hành và bảo trì quy đổi theo giờ)


### **Cơ chế AMOS làm giảm LCOH proxy (có thể kiểm toán)**
AMOS làm giảm $LCOH_{proxy}$ thông qua ba cơ chế **định lượng và kiểm chứng được** :
  1. **Tăng uptime ($U$)**
     * Giảm trip và dừng ngoài kế hoạch.
     * Làm tăng trực tiếp $Q_{eff}$ (mẫu số).


  2. **Kéo dài tuổi thọ hữu dụng ($Life_h$)**
     * Cấm boost sai điều kiện.
     * Giảm tốc độ suy giảm vật liệu.
     * Làm giảm $C_{cap,h}$ theo thời gian.


  3. **Giảm can thiệp và chi phí bảo trì**
     * Derate sớm thay cho shutdown.
     * Giảm số lần can thiệp thủ công và downtime.
     * Làm giảm $C_{maint,h}$ và chi phí ẩn do dừng máy.


LCOH proxy **không dùng để thay thế LCOH chuẩn** , nhưng là công cụ hợp lệ để:
  * so sánh phương án thiết kế,


  * đánh giá tác động của logic điều khiển lên chi phí vòng đời,


  * trình bày rõ lợi thế vận hành của AMOS trong hồ sơ kỹ thuật.


Chỉ số này phản ánh đúng triết lý của AMOS: **giảm chi phí hydro bằng kiểm soát vận hành và suy giảm** , không bằng tối ưu thông số danh định ngắn hạn.
# **6) Có đạt chuẩn khắt khe nhất và vượt SOTA không?”**
## **6.1. Yêu cầu để được công nhận “đạt chuẩn khắt khe”**
Hệ thống **có khả năng đáp ứng các chuẩn nghiêm ngặt** nếu thiết kế và triển khai đầy đủ bốn trụ an toàn sau:
  1. **An toàn điện / điện tử**
     * Bảo vệ quá áp, quá dòng, ngắn mạch.
     * Cách ly, nối đất, và kiểm soát EMI/EMC theo chuẩn áp dụng.


  2. **An toàn chức năng (Functional Safety)**
     * Tối thiểu có **kênh an toàn độc lập** với kênh điều khiển chính.
     * Các trạng thái Protective/Lockout không phụ thuộc phần mềm điều khiển công suất.


  3. **An toàn hydro**
     * Phát hiện rò rỉ, giám sát áp suất, interlock phần cứng.
     * Quy định rõ khu vực lắp đặt, thông gió, và trình tự dừng an toàn.


  4. **An ninh mạng công nghiệp (nếu có giám sát/điều khiển từ xa)**
     * Phân tách mạng điều khiển và mạng giám sát.
     * Cơ chế xác thực, ghi log truy cập, và cập nhật có kiểm soát.


**Lưu ý thẩm định:**
Việc “được công nhận đạt chuẩn” **không dựa trên tuyên bố thiết kế** , mà yêu cầu đầy đủ:
  * kế hoạch thử nghiệm (test plan),


  * dữ liệu thử nghiệm thực tế,


  * log vận hành và audit trail,


  * ma trận truy vết: **yêu cầu → thiết kế → kiểm thử → kết quả**.


Thiếu bất kỳ thành phần nào trong chuỗi này, hệ thống chỉ được xem là “có khả năng đáp ứng”, chưa phải “được chứng nhận”.
## **6.2. Cách tiếp cận đúng khi tuyên bố “vượt SOTA”**
  * **Không nên** tuyên bố vượt SOTA dựa trên một chỉ số đơn lẻ như hiệu suất L/kWh hoặc thông số danh định.


  * **Có thể tuyên bố vượt SOTA** ở các khía cạnh mà công nghệ hiện hành thường yếu hoặc khó chứng minh, bao gồm:
    * uptime vận hành dài hạn,
    * MTBC (Mean Time Between Correction),
    * tần suất can thiệp của con người,
    * chi phí vòng đời (LCOH thực tế),
    * hồ sơ an toàn có thể kiểm toán.


**Điều kiện bắt buộc để tuyên bố hợp lệ:**
  * vận hành dài hạn có kiểm soát (ví dụ 1.000 h / 3.000 h),


  * dữ liệu log đầy đủ, liên tục,


  * thống kê sự cố, can thiệp và suy giảm,


  * phương pháp đánh giá rõ ràng và có thể lặp lại.


Chỉ khi các điều kiện trên được đáp ứng, tuyên bố “vượt SOTA” mới có giá trị kỹ thuật và được hội đồng chấp nhận.
# **KẾ HOẠCH TRIỂN KHAI AMOS-IKONOMY (2025–2032)**
* * *
## **GIAI ĐOẠN 1 — CỐ ĐỊNH THIẾT KẾ & CHỨNG MINH KỸ THUẬT CỐT LÕI**
**(0–9 tháng | mục tiêu: “đứng vững về kỹ thuật”)**
### **1.1. Mục tiêu**
  * Khóa thiết kế **AMOS-IKONOMY module 1 kW** ở mức:
    * vận hành ổn định,
    * logic AMOS hoàn chỉnh,
    * đủ dữ liệu để nói chuyện với hội đồng / đối tác nghiêm túc.


  * Chuyển từ “thiết kế hợp lý” → **thiết kế có chứng cứ**.


### **1.2. Việc phải làm (technical deliverables)**
  1. Hoàn thiện **bản thiết kế cuối (design freeze)** :
     * power stage (buck/buck-boost),
     * sensing,
     * firmware AMOS,
     * state machine đầy đủ (Cruise / Boost / Degraded / Protective / Lockout).


  2. Chạy **test dài hạn bắt buộc** :
     * 1.000–3.000 giờ liên tục,
     * nguồn dao động ±15%,
     * mô phỏng điều kiện nóng/ẩm VN.


  3. Thu thập **log & audit trail**:
     * uptime,
     * số lần boost,
     * số lần từ chối boost,
     * số lần derate,
     * không có “trip vô cớ”.


### **1.3. KPI kỹ thuật cần đạt**
  * Uptime ≥ **97–98%**


  * Trip ≤ **1–3 lần / 1.000 giờ**


  * Boost hoạt động đúng “ngân sách” (không vượt)


  * Không hỏng stack sớm


### **1.4. Giá trị tạo ra**
  * Chứng minh **AMOS không phải lý thuyết**.


  * Có dữ liệu thật để:
    * xin tài trợ,
    * gọi vốn seed,
    * hoặc ký MoU pilot.


* * *
## **GIAI ĐOẠN 2 — PILOT THỰC ĐỊA (10–100 MODULE)**
**(9–18 tháng | mục tiêu: “đứng vững trong thế giới thật”)**
### **2.1. Mục tiêu**
  * Đưa AMOS-IKONOMY ra **điều kiện sử dụng thật** :
    * cảng,
    * khu công nghiệp nhỏ,
    * đảo / off-grid,
    * RES dao động.


### **2.2. Quy mô**
  * 10–100 module (10–100 kW)


  * Triển khai phân tán (không gom 1 chỗ).


### **2.3. Việc phải làm**
  1. Chuẩn hóa:
     * quy trình lắp đặt,
     * quy trình vận hành,
     * quy trình bảo trì (SOP).


  2. Đo **chi phí thực** :
     * điện / kg H₂,
     * thời gian can thiệp con người,
     * downtime thực tế.


  3. Hoàn thiện **hồ sơ chuẩn hóa** :
     * ISO 22734 (electrolyzer),
     * IEC 61010/60204 (an toàn),
     * chuẩn bị cho IEC 61508 (an toàn chức năng).


### **2.4. KPI kinh tế**
  * LCOH thực tế ≤ **4–6 USD/kg** (điện VN)


  * MTBC ≥ **500 giờ**


  * Nhân lực vận hành ≤ **0,1–0,2 FTE / 100 kW**


### **2.5. Giá trị tạo ra**
  * Chứng minh AMOS **giảm OPEX thật**.


  * Có case study đủ mạnh để:
    * bán hàng,
    * xin dự án lớn,
    * nâng định giá công ty.


* * *
## **GIAI ĐOẠN 3 — SẢN XUẤT CÔNG NGHIỆP NHỎ (1–10 MW)**
**(18–30 tháng | mục tiêu: “bắt đầu kiếm tiền thật”)**
### **3.1. Mục tiêu**
  * Chuyển từ pilot → **doanh thu ổn định**.


  * Chuẩn hóa sản xuất tại Việt Nam.


### **3.2. Quy mô**
  * 1–10 MW lắp đặt/năm
(≈ 1.000–10.000 module/năm)


### **3.3. Mô hình kinh doanh**
  * **Kết hợp 2 mô hình** :
    1. Bán module (CAPEX)
    2. O&M + AMOS software (recurring)


### **3.4. Doanh thu ước tính (bảo thủ)**
  * 1 MW:
    * Doanh thu thiết bị: ~1–3 triệu USD
    * Dịch vụ/O&M: 0,2–0,5 triệu USD/năm


  * 10 MW:
    * Doanh thu: **10–30 triệu USD**
    * Lợi nhuận gộp: **25–40%**


### **3.5. Giá trị tạo ra**
  * Dòng tiền thật.


  * Thoát khỏi “startup nghiên cứu”.


* * *
## **GIAI ĐOẠN 4 — CỤM MW PHÂN TÁN & H₂-AS-A-SERVICE**
**(30–48 tháng | mục tiêu: “ăn vào chuỗi giá trị”)**
### **4.1. Mục tiêu**
  * Không chỉ bán máy → **bán hydro + dịch vụ**.


  * Định giá doanh nghiệp cao hơn (recurring revenue).


### **4.2. Quy mô**
  * 50–100 MW phân tán


  * Ứng dụng:
    * logistics,
    * cảng,
    * công nghiệp vừa,
    * đảo.


### **4.3. Doanh thu**
  * 100 MW:
    * Sản lượng: ~13.000 tấn H₂/năm
    * Doanh thu: **80–130 triệu USD/năm**
    * Lợi nhuận gộp: **30–50 triệu USD/năm** (nếu biên 2–4 USD/kg)


### **4.4. Giá trị tạo ra**
  * AMOS trở thành **hạ tầng** , không còn là “thiết bị”.


* * *
## **GIAI ĐOẠN 5 — SCALE LÊN GW & XUẤT KHẨU**
**(4–7 năm | mục tiêu: “significant toàn cầu”)**
### **5.1. Mục tiêu**
  * Xuất khẩu module + AMOS logic.


  * Đánh vào thị trường:
    * SEA,
    * Ấn Độ,
    * châu Phi,
    * Mỹ Latinh.


### **5.2. Quy mô**
  * 0,5–1 GW phân tán


  * Doanh thu tiềm năng: **0,8–1,3 tỷ USD/năm**


### **5.3. Lợi thế cạnh tranh**
  * Uptime cao trong môi trường khó.


  * Không cần đội kỹ sư dày.


  * Audit + safety + cybersecurity sẵn sàng.


* * *
## **GIAI ĐOẠN 6 — MOAT DÀI HẠN (10+ NĂM)**
### **6.1. Thứ giữ bạn không bị sao chép**
  * AMOS logic + audit trail + safety case.


  * Dữ liệu vận hành tích lũy hàng triệu giờ.


  * Chuẩn hóa “how to run electrolyzer safely”.


### **6.2. Định vị cuối**
AMOS-IKONOMY không chỉ là:
> “máy điện phân nhỏ”
mà là:
> nền tảng vận hành hydro phân tán an toàn – bền – kiểm toán được
* * *
# **KẾT LUẬN THẲNG**
  * **Có, nó significant** – không phải vì nhỏ hay lớn, mà vì **nó scale được và giảm chi phí vòng đời ở nơi thị trường đang đau**.


  * **Tiền không nằm ở 1 kW** , mà nằm ở:
    * 100 MW → hàng chục triệu USD/năm,
    * 1 GW → hàng tỷ USD/năm.


  * AMOS là thứ biến “kỹ thuật tốt” thành **doanh nghiệp lớn**.


\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
