### Bài tập ch08_ex01 (Slide 7, Trang 4): Thiết kế Bể Phản ứng Kỵ khí Khuấy trộn Hoàn toàn

**Đề bài** (Lời giải khôi phục theo chuẩn slide của thầy từ Slide 5–7): Thiết kế hệ thống bể phản ứng kỵ khí khuấy trộn hoàn toàn có tuần hoàn bùn để xử lý lưu lượng nước thải $Q = 500\text{ m}^3/\text{d}$ ở nhiệt độ vận hành $T = 25^\circ\text{C}$ với tổng nồng độ $\text{COD} = 6000\text{ g/m}^3$, phần hòa tan $\text{sCOD} = 4000\text{ g/m}^3$ và yêu cầu hiệu suất khử đạt $E = 90\%$ [Page 4].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng nước thải đầu vào | $Q$ | $500$ | $\text{m}^3/\text{d}\text{ (Slide 7)}$ |
| Tổng nhu cầu oxy hóa học | $\text{COD}$ | $6000$ | $\text{g/m}^3\text{ (Slide 7)}$ |
| Nhu cầu oxy hóa học hòa tan | $\text{sCOD}$ | $4000$ | $\text{g/m}^3\text{ (Slide 7)}$ |
| Tỷ số $\text{COD}$ trên chất rắn bay hơi | $\text{COD}/\text{VSS}$ | $1.8$ | $\text{g/g}\text{ (Slide 7)}$ |
| Tỷ lệ $\text{VSS}$ phân hủy sinh học | $f_{\text{deg}}$ | $80\%$ | $\%\text{ (Slide 7)}$ |
| Nồng độ Nitơ và Photpho đầu vào | $\text{N}_0,\; \text{P}_0$ | $10,\; 20$ | $\text{g/m}^3\text{ (Slide 7)}$ |
| Độ kiềm nước thải đầu vào | $\text{Alk}_0$ | $500$ | $\text{g CaCO}_3/\text{m}^3\text{ (Slide 7)}$ |
| Nhiệt độ vận hành bể kỵ khí | $T$ | $25$ | $^\circ\text{C}\text{ (Slide 7)}$ |
| Nồng độ cặn bay hơi đầu ra | $\text{VSS}_e$ | $150$ | $\text{g/m}^3\text{ (Slide 7)}$ |
| Hệ số mảnh vụn tế bào | $f_d$ | $0.15$ | $\text{g/g}\text{ (Slide 7)}$ |
| Nồng độ bùn kỵ khí trong bể | $X_{\text{MLVSS}}$ | $6000$ | $\text{g/m}^3\text{ (Slide 7)}$ |
| Thành phần khí sinh học | $\%_{\text{CH}_4},\; \%_{\text{CO}_2}$ | $65\%,\; 35\%$ | $\%\text{ (Slide 7)}$ |
| Hàm lượng dinh dưỡng trong sinh khối | $f_{\text{N}},\; f_{\text{P}}$ | $12\%,\; 2.4\%$ | $\%\text{ (Slide 7)}$ |
| Tải trọng bề mặt bể lắng thứ cấp | $\text{OFR}$ | $24$ | $\text{m}^3/\text{m}^2\cdot\text{d}\text{ (Slide 7)}$ |
| Hiệu suất khử $\text{COD}$ yêu cầu | $E$ | $90\%$ | $\%\text{ (Slide 7)}$ |
| Hệ số an toàn tuổi bùn | $\text{FS}$ | $3.0$ | $\text{Không thứ nguyên (Slide 7)}$ |
| Hệ số sản lượng và phân hủy nội bào | $Y,\; k_d$ | $0.08,\; 0.03$ | $\text{g/g},\; \text{d}^{-1}\text{ (Slide 5)}$ |
| Tốc độ sinh trưởng cực đại và hằng số $K_s$ | $\mu_m,\; K_s$ | $0.20,\; 120$ | $\text{d}^{-1},\; \text{g/m}^3\text{ (Slide 5)}$ |

**Bước 1 - Phân tách thành phần $\text{COD}$ và $\text{VSS}$ đầu vào**: Nồng độ $\text{pCOD}$ dạng hạt đạt $2000\text{ g/m}^3$, nồng độ cặn $\text{VSS}_0$ bằng $1111.1\text{ g/m}^3$ và phần cặn trơ $\text{nbVSS}$ bằng $222.2\text{ g/m}^3$. Tổng cơ chất dễ phân hủy $S_0$ đạt $5600\text{ g/m}^3$, cơ chất đầu ra $S$ còn $560\text{ g/m}^3$ và độ giảm $\Delta S$ đạt $5040\text{ g/m}^3$ [Page 4].

$$\text{pCOD} = \text{COD} - \text{sCOD} = 6000 - 4000 = 2000\text{ g/m}^3$$

$$\text{VSS}_0 = \frac{\text{pCOD}}{1.8} = \frac{2000}{1.8} = 1111.1\text{ g/m}^3$$

$$\text{nbVSS} = (1 - 0.80)\times 1111.1 = 222.2\text{ g/m}^3$$

$$S_0 = 4000 + 0.80\times 2000 = 5600\text{ g/m}^3$$

$$S = (1 - 0.90)\times 5600 = 560\text{ g/m}^3$$

**Bước 2 - Xác định tuổi bùn cực tiểu và tuổi bùn thiết kế $\theta_c$**: Theo phương trình động học Monod trên Slide 5 ở $25^\circ\text{C}$, tuổi bùn cực tiểu $\theta_{c,\min}$ bằng $7.42\text{ d}$. Nhân với hệ số an toàn $\text{FS} = 3.0$, tuổi bùn thiết kế $\theta_c$ đạt $22.3\text{ d}$ [Page 3].

$$\frac{1}{\theta_{c,\min}} = \frac{\mu_m S}{K_s + S} - k_d$$

$$\frac{1}{\theta_{c,\min}} = \frac{0.20\times 560}{120 + 560} - 0.03 = 0.1347\text{ d}^{-1}$$

$$\theta_{c,\min} = \frac{1}{0.1347} = 7.42\text{ d}$$

$$\theta_c = \text{FS}\times \theta_{c,\min} = 3.0\times 7.42 = 22.3\text{ d}$$

**Bước 3 - Tính lượng bùn sinh ra mỗi ngày và khối lượng bùn trong bể**: Lượng sinh khối kỵ khí tổng hợp $P_{x,\text{bio}}$ đạt $133.0\text{ kg/d}$ và phần cặn trơ đi vào $P_{x,\text{nb}}$ bằng $111.1\text{ kg/d}$. Tổng sản lượng bùn $P_{x,\text{VSS}}$ đạt $244.1\text{ kg/d}$ và tổng lượng bùn giữ trong bể $M_{\text{VSS}}$ bằng $5443.4\text{ kg}$ [Page 3].

$$P_{x,\text{bio}} = \frac{Q Y (S_0 - S)(1 + f_d k_d \theta_c)}{(1 + k_d \theta_c)\times 10^3}$$

$$P_{x,\text{bio}} = \frac{500\times 0.08\times 5040\times (1 + 0.15\times 0.03\times 22.3)}{(1 + 0.03\times 22.3)\times 10^3} = 133.0\text{ kg/d}$$

$$P_{x,\text{VSS}} = 133.0 + \frac{500\times 222.2}{10^3} = 244.1\text{ kg/d}$$

$$M_{\text{VSS}} = P_{x,\text{VSS}}\times \theta_c = 5443.4\text{ kg}$$

**Bước 4 - Xác định thể tích bể phản ứng, thời gian lưu và bể lắng**: Với nồng độ bùn $X_{\text{MLVSS}}$ bằng $6.0\text{ kg/m}^3$, thể tích bể phản ứng $V$ đạt $907.2\text{ m}^3$ và thời gian lưu nước $\text{HRT}$ bằng $43.5\text{ h}$. Diện tích bể lắng thứ cấp $A_c$ đạt $20.83\text{ m}^2$, tương ứng đường kính $D_c = 5.15\text{ m}$ [Page 4].

$$V = \frac{M_{\text{VSS}}}{X_{\text{MLVSS}}} = \frac{5443.4}{6.0} = 907.2\text{ m}^3$$

$$\text{HRT} = \frac{V}{Q}\times 24 = \frac{907.2}{500}\times 24 = 43.5\text{ h}$$

$$A_c = \frac{Q}{\text{OFR}} = \frac{500}{24} = 20.83\text{ m}^2$$

$$D_c = \sqrt{\frac{4 A_c}{\pi}} = \sqrt{\frac{4\times 20.83}{\pi}} = 5.15\text{ m}$$

**Bước 5 - Tính sản lượng khí metan và tổng lưu lượng khí sinh học**: Từ cân bằng $\text{COD}$, lượng chất hữu cơ chuyển thành khí metan $\text{COD}_{\text{CH}_4}$ đạt $2331.1\text{ kg/d}$. Quy đổi hệ số $0.35\text{ m}^3/\text{kg}$ từ $0^\circ\text{C}$ sang $25^\circ\text{C}$, lưu lượng metan $V_{\text{CH}_4}$ đạt $890.6\text{ m}^3/\text{d}$ và tổng khí sinh học $V_{\text{gas}}$ đạt $1370.1\text{ m}^3/\text{d}$ [Page 3].

$$\text{COD}_{\text{CH}_4} = \frac{Q(S_0 - S)}{10^3} - 1.42 P_{x,\text{bio}}$$

$$\text{COD}_{\text{CH}_4} = 2520.0 - 1.42\times 133.0 = 2331.1\text{ kg/d}$$

$$V_{\text{CH}_4} = 2331.1\times 0.35\times \frac{273.15 + 25}{273.15} = 890.6\text{ m}^3/\text{d}$$

$$V_{\text{gas}} = \frac{890.6}{0.65} = 1370.1\text{ m}^3/\text{d}$$

**Bước 6 - Tính lượng bùn dư xả bỏ và nhu cầu bổ sung dinh dưỡng**: Trừ lượng bùn trôi theo dòng ra $75.0\text{ kg/d}$, lượng bùn dư cần xả bỏ $W_{\text{waste}}$ bằng $169.1\text{ kg/d}$. Nhu cầu Nitơ cần bổ sung $\Delta\text{N}$ là $10.96\text{ kg/d}$, còn lượng Photpho đầu vào $10.0\text{ kg/d}$ đã vượt nhu cầu $3.19\text{ kg/d}$ [Page 4].

$$W_{\text{waste}} = P_{x,\text{VSS}} - \frac{Q\times \text{VSS}_e}{10^3}$$

$$W_{\text{waste}} = 244.1 - \frac{500\times 150}{10^3} = 244.1 - 75.0 = 169.1\text{ kg/d}$$

$$\Delta\text{N} = 0.12 P_{x,\text{bio}} - \frac{Q\times \text{N}_0}{10^3} = 15.96 - 5.00 = 10.96\text{ kg/d}$$

$$\text{P}_{\text{req}} = 0.024\times 133.0 = 3.19\text{ kg/d}$$

**Bước 7 - Kiểm tra tải trọng hữu cơ thể tích và tính độ kiềm bổ sung**: Tải trọng hữu cơ thể tích $\text{OLR}$ của bể đạt $3.31\text{ kg COD/m}^3\text{d}$. Để giữ $\text{pH} = 7.0$ ứng với $35\%\text{ CO}_2$ cần độ kiềm $2500\text{ g/m}^3$, do đó khối lượng độ kiềm cần châm thêm $M_{\text{Alk}}$ bằng $1000\text{ kg CaCO}_3/\text{d}$ [Page 4].

$$\text{OLR} = \frac{Q\times \text{COD}}{V\times 10^3}$$

$$\text{OLR} = \frac{500\times 6000}{907.2\times 10^3} = 3.31\text{ kg COD/m}^3\cdot\text{d}$$

$$M_{\text{Alk}} = \frac{Q(\text{Alk}_{\text{req}} - \text{Alk}_0)}{10^3}$$

$$M_{\text{Alk}} = \frac{500\times (2500 - 500)}{10^3} = 1000.0\text{ kg CaCO}_3/\text{d}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Tuổi bùn kỵ khí thiết kế ($\theta_c$)**: $22.3\text{ d}$ (Kiểm tra: $15\text{ d} \le \theta_c \le 30\text{ d}\text{ - Đạt chuẩn Slide 3}$)
- **Tổng sản lượng bùn sinh ra ($P_{x,\text{VSS}}$)**: $244.1\text{ kg VSS/d}$ (Kiểm tra: $P_{x,\text{bio}} = 133.0\text{ kg/d}\text{ - Đạt chuẩn Slide 6}$)
- **Thể tích bể phản ứng kỵ khí ($V$)**: $907.2\text{ m}^3$ (Kiểm tra: $\text{HRT} = 43.5\text{ h},\; X_{\text{MLVSS}} = 6000\text{ g/m}^3\text{ - Đạt chuẩn Slide 3}$)
- **Diện tích và đường kính bể lắng ($A_c,\; D_c$)**: $20.83\text{ m}^2,\; 5.15\text{ m}$ (Kiểm tra: $\text{OFR} = 24\text{ m}^3/\text{m}^2\cdot\text{d}\text{ - Đạt chuẩn Slide 7}$)
- **Lưu lượng khí metan và tổng khí sinh học ($V_{\text{CH}_4},\; V_{\text{gas}}$)**: $890.6\text{ m}^3/\text{d},\; 1370.1\text{ m}^3/\text{d}$ (Kiểm tra: $\%_{\text{CH}_4} = 65\%\text{ ở } 25^\circ\text{C}\text{ - Đạt chuẩn Slide 5}$)
- **Tải trọng hữu cơ thể tích ($\text{OLR}$)**: $3.31\text{ kg COD/m}^3\cdot\text{d}$ (Kiểm tra: $2\text{ kg/m}^3\cdot\text{d} \le \text{OLR} \le 5\text{ kg/m}^3\cdot\text{d}\text{ - Đạt chuẩn Slide 3}$)
- **Lượng bùn xả bỏ và hóa chất bổ sung ($W_{\text{waste}},\; \Delta\text{N},\; M_{\text{Alk}}$)**: $169.1\text{ kg VSS/d},\; 10.96\text{ kg N/d},\; 1000\text{ kg CaCO}_3/\text{d}$ (Kiểm tra: $\text{pH} \approx 7.0\text{ - Đạt chuẩn Slide 6}$)

### Bài tập ch08_ex02 (Slide 21, Trang 7): Thiết kế Bể Phản ứng Kỵ khí Dòng chảy Ngược qua Tầng Bùn (UASB)

**Đề bài** (Lời giải khôi phục theo chuẩn slide của thầy từ Slide 19–21): Thiết kế công trình xử lý kỵ khí dòng chảy ngược qua tầng bùn (UASB) cho lưu lượng $Q = 500\text{ m}^3/\text{d}$ ở nhiệt độ $T = 25^\circ\text{C}$ với nồng độ đầu vào $\text{COD} = 12,000\text{ g/m}^3$, $\text{TSS} = 600\text{ g/m}^3$, $\text{nbVSS} = 500\text{ g/m}^3$, tải trọng thiết kế $\text{OLR} = 8\text{ kg COD/m}^3\cdot\text{d}$ và hiệu suất khử $E = 90\%$ [Page 7].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng nước thải đầu vào | $Q$ | $500$ | $\text{m}^3/\text{d}\text{ (Slide 21)}$ |
| Nồng độ $\text{COD}$ đầu vào | $S_0$ | $12,000$ | $\text{g/m}^3\text{ (Slide 21)}$ |
| Tổng chất rắn lơ lửng đầu vào | $\text{TSS}$ | $600$ | $\text{g/m}^3\text{ (Slide 21)}$ |
| Cặn bay hơi không phân hủy sinh học | $\text{nbVSS}$ | $500$ | $\text{g/m}^3\text{ (Slide 21)}$ |
| Độ kiềm nước thải đầu vào | $\text{Alk}_0$ | $500$ | $\text{g CaCO}_3/\text{m}^3\text{ (Slide 21)}$ |
| Nhiệt độ vận hành bể UASB | $T$ | $25$ | $^\circ\text{C}\text{ (Slide 21)}$ |
| Tải trọng hữu cơ thiết kế | $\text{OLR}$ | $8.0$ | $\text{kg COD/m}^3\cdot\text{d}\text{ (Slide 21)}$ |
| Hiệu suất khử $\text{COD}$ thiết kế | $E$ | $90\%$ | $\%\text{ (Slide 21)}$ |
| Nồng độ cặn bay hơi đầu ra | $\text{VSS}_e$ | $120$ | $\text{g/m}^3\text{ (Slide 21)}$ |
| Nồng độ bùn trong tầng chăn bùn | $X_{\text{MLVSS}}$ | $30,000$ | $\text{g/m}^3\text{ (Slide 21)}$ |
| Hệ số mảnh vụn tế bào | $f_d$ | $0.10$ | $\text{g/g}\text{ (Slide 21)}$ |
| Tỷ lệ khí metan và cacbon dioxit | $\%_{\text{CH}_4},\; \%_{\text{CO}_2}$ | $65\%,\; 35\%$ | $\%\text{ (Slide 21)}$ |
| Chiều cao vùng phản ứng và vùng trong | $H_p,\; H_{\text{clear}}$ | $6.0,\; 0.5$ | $\text{m}\text{ (Slide 21)}$ |
| Chiều cao bộ tách khí-rắn và tỷ số $L/W$ | $H_{\text{GLSS}},\; L/W$ | $1.5,\; 2.0$ | $\text{m},\; \text{Không thứ nguyên (Slide 21)}$ |
| Hệ số sản lượng và phân hủy nội bào | $Y,\; k_d$ | $0.08,\; 0.03$ | $\text{g/g},\; \text{d}^{-1}\text{ (Slide 5)}$ |

**Bước 1 - Xác định thể tích vùng phản ứng và diện tích mặt cắt ngang**: Tổng tải lượng hữu cơ đầu vào đạt $6000\text{ kg COD/d}$, nên tại tải trọng $\text{OLR}$ bằng $8\text{ kg COD/m}^3\text{d}$ thể tích vùng phản ứng $V_p$ bằng $750\text{ m}^3$. Với chiều cao vùng phản ứng $H_p = 6.0\text{ m}$, diện tích mặt bằng bể $A$ đạt $125\text{ m}^2$ [Page 7].

$$V_p = \frac{Q S_0}{\text{OLR}\times 10^3}$$

$$V_p = \frac{500\times 12,000}{8.0\times 10^3} = \frac{6000}{8.0} = 750.0\text{ m}^3$$

$$A = \frac{V_p}{H_p} = \frac{750.0}{6.0} = 125.0\text{ m}^2$$

$$\text{HRT} = \frac{V_p}{Q}\times 24 = 36.0\text{ h}$$

**Bước 2 - Tính kích thước hình học bể và kiểm tra vận tốc dòng chảy ngược**: Với tỷ số chiều dài trên chiều rộng $L/W = 2$, chiều rộng bể $W$ bằng $7.91\text{ m}$ (chọn $8.0\text{ m}$), chiều dài $L$ bằng $15.81\text{ m}$ (chọn $16.0\text{ m}$) và tổng chiều cao $H_{\text{tot}}$ bằng $7.5\text{ m}$. Vận tốc dòng chảy ngược $v$ đạt $0.167\text{ m/h}$ [Page 6].

$$W = \sqrt{\frac{A}{2}} = \sqrt{\frac{125.0}{2}} = 7.91\text{ m}$$

$$L = 2W = 15.81\text{ m}$$

$$H_{\text{tot}} = 6.0 + 1.5 = 7.5\text{ m}$$

$$v = \frac{Q}{24 A} = \frac{500}{24\times 125.0} = \frac{20.83}{125.0} = 0.167\text{ m/h}$$

**Bước 3 - Tính thể tích tầng bùn và tổng khối lượng sinh khối lưu giữ**: Trừ chiều cao vùng nước trong $H_{\text{clear}}$ bằng $0.5\text{ m}$, chiều cao thực tế của tầng bùn $H_{\text{sb}}$ bằng $5.5\text{ m}$ và thể tích tầng bùn $V_{\text{sb}}$ đạt $687.5\text{ m}^3$. Ở nồng độ $X_{\text{MLVSS}}$ bằng $30\text{ kg/m}^3$, tổng khối lượng bùn giữ trong bể $M_{\text{VSS}}$ đạt $20,625\text{ kg}$ [Page 7].

$$H_{\text{sb}} = H_p - H_{\text{clear}} = 6.0 - 0.5 = 5.5\text{ m}$$

$$V_{\text{sb}} = A\times H_{\text{sb}} = 125.0\times 5.5 = 687.5\text{ m}^3$$

$$M_{\text{VSS}} = V_{\text{sb}}\times X_{\text{MLVSS}} = 687.5\times 30.0 = 20,625.0\text{ kg VSS}$$

**Bước 4 - Xác định tuổi bùn $\theta_c$, sản lượng bùn và lượng bùn dư xả bỏ**: Lượng chất hữu cơ khử mỗi ngày $\Delta\text{COD}$ bằng $5400\text{ kg/d}$ và lượng cặn trơ vào bể bằng $250\text{ kg/d}$. Giải phương trình cân bằng khối lượng bùn cho tuổi bùn $\theta_c = 45.0\text{ d}$, sản lượng sinh khối $P_{x,\text{bio}}$ bằng $208.7\text{ kg/d}$, tổng bùn $P_{x,\text{VSS}}$ bằng $458.7\text{ kg/d}$ và bùn xả bỏ $W_{\text{waste}}$ bằng $398.7\text{ kg/d}$ [Page 6].

$$M_{\text{VSS}} = \theta_c\left[\frac{Y\Delta\text{COD}(1 + f_d k_d \theta_c)}{1 + k_d \theta_c} + \frac{Q\cdot \text{nbVSS}}{10^3}\right]$$

$$M_{\text{VSS}} = 20,625.0\text{ kg} \implies \theta_c = 45.0\text{ d}$$

$$P_{x,\text{bio}} = \frac{0.08\times 5400\times (1 + 0.10\times 0.03\times 45.0)}{1 + 0.03\times 45.0} = 208.7\text{ kg/d}$$

$$P_{x,\text{VSS}} = 458.7\text{ kg/d}$$

$$W_{\text{waste}} = P_{x,\text{VSS}} - \frac{Q\times \text{VSS}_e}{10^3}$$

$$W_{\text{waste}} = 458.7 - \frac{500\times 120}{10^3} = 458.7 - 60.0 = 398.7\text{ kg/d}$$

**Bước 5 - Tính sản lượng khí metan và tổng lưu lượng khí sinh học ở $25^\circ\text{C}$**: Lượng $\text{COD}$ chuyển hóa thành khí metan $\text{COD}_{\text{CH}_4}$ đạt $5103.7\text{ kg/d}$. Quy đổi hệ số $0.35\text{ m}^3/\text{kg}$ sang nhiệt độ vận hành $25^\circ\text{C}$, lưu lượng khí metan $V_{\text{CH}_4}$ đạt $1949.8\text{ m}^3/\text{d}$ và tổng lưu lượng khí sinh học $V_{\text{gas}}$ đạt $2999.7\text{ m}^3/\text{d}$ [Page 7].

$$\text{COD}_{\text{CH}_4} = \Delta\text{COD} - 1.42 P_{x,\text{bio}} = 5400.0 - 1.42\times 208.7 = 5103.7\text{ kg/d}$$

$$V_{\text{CH}_4} = 5103.7\times 0.35\times \frac{298.15}{273.15} = 1949.8\text{ m}^3/\text{d}$$

$$V_{\text{gas}} = \frac{1949.8}{0.65} = 2999.7\text{ m}^3/\text{d}$$

**Bước 6 - Kiểm tra nhu cầu dinh dưỡng tối thiểu và độ kiềm bổ sung**: Theo tỷ lệ chuẩn $625:5:1:1$ của $(\text{COD}/Y)$ đối với $\text{N}$, $\text{P}$ và $\text{S}$ trên Slide 29, nồng độ tối thiểu cần duy trì là $\text{N}_{\min}$ bằng $96\text{ g/m}^3$ và $\text{P}_{\min}$ bằng $\text{S}_{\min}$ bằng $19.2\text{ g/m}^3$. Lượng độ kiềm cần bổ sung $M_{\text{Alk}}$ bằng $1000\text{ kg CaCO}_3/\text{d}$ [Page 7].

$$\text{N}_{\min} = 12,000\times \frac{5}{625} = 96.0\text{ g/m}^3$$

$$\text{P}_{\min} = \text{S}_{\min} = 12,000\times \frac{1}{625} = 19.2\text{ g/m}^3$$

$$M_{\text{Alk}} = \frac{Q(\text{Alk}_{\text{req}} - \text{Alk}_0)}{10^3}$$

$$M_{\text{Alk}} = \frac{500\times (2500 - 500)}{10^3} = 1000.0\text{ kg CaCO}_3/\text{d}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Thể tích vùng phản ứng và diện tích bể ($V_p,\; A$)**: $750.0\text{ m}^3,\; 125.0\text{ m}^2$ (Kiểm tra: $\text{OLR} = 8.0\text{ kg COD/m}^3\cdot\text{d} \in [5,\; 15]\text{ - Đạt chuẩn Slide 20}$)
- **Kích thước hình học bể UASB ($W \times L \times H_{\text{tot}}$)**: $7.91\text{ m} \times 15.81\text{ m} \times 7.5\text{ m}$ (Kiểm tra: $H_p = 6.0\text{ m} \in [3,\; 7]\text{ m}\text{ - Đạt chuẩn Slide 19}$)
- **Vận tốc dòng chảy ngược ($v$)**: $0.167\text{ m/h}$ (Kiểm tra: $v < 1.0\text{ m/h}\text{ cho nước thải có cặn - Đạt chuẩn Slide 19}$)
- **Khối lượng bùn và tuổi bùn thực tế ($M_{\text{VSS}},\; \theta_c$)**: $20,625\text{ kg VSS},\; 45.0\text{ d}$ (Kiểm tra: $\theta_c \in [30,\; 60]\text{ d}\text{ - Đạt chuẩn Slide 19}$)
- **Sản lượng bùn và lượng bùn xả bỏ ($P_{x,\text{VSS}},\; W_{\text{waste}}$)**: $458.7\text{ kg VSS/d},\; 398.7\text{ kg VSS/d}$ (Kiểm tra: $\text{VSS}_e = 120\text{ g/m}^3\text{ - Đạt chuẩn Slide 21}$)
- **Lưu lượng khí metan và tổng khí sinh học ($V_{\text{CH}_4},\; V_{\text{gas}}$)**: $1949.8\text{ m}^3/\text{d},\; 2999.7\text{ m}^3/\text{d}$ (Kiểm tra: $\%_{\text{CH}_4} = 65\%\text{ ở } 25^\circ\text{C}\text{ - Đạt chuẩn Slide 21}$)
