### Bài tập ch02_ex01 (Slide 17 đến 21 - Example 1): Thiết kế thể tích bể điều hòa, công suất khuấy trộn và lưu lượng khí cấp

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy]): Xác định thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$), thể tích bể điều hòa thực tế ($V_{\text{prac}}$), công suất khuấy trộn cơ học ($P_{\text{mix}}$) và lưu lượng không khí cần cấp ($Q_{\text{air}}$) cho trạm xử lý nước thải có dữ liệu lưu lượng đầu vào trong $24\text{ giờ}$ trên Slide 17 biến thiên từ cực tiểu $Q_{\min} = 360\text{ m}^3\text{/h}$ (khung giờ $5\text{–}6$) đến cực đại $Q_{\max} = 1548\text{ m}^3\text{/h}$ (khung giờ $11\text{–N}$) [Page 5] [Page 6] [Page 9].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Tổng thể tích nước thải trong $24\text{ giờ}$ | $\sum V_{\text{in}}$ | $26,550$ | $\text{m}^3\text{/ngày}$ (Slide 18, Ảnh #02) |
| Lưu lượng bơm ra trung bình mỗi giờ | $Q_{\text{avg}}$ | $1106.25$ | $\text{m}^3\text{/h}$ (Slide 18, Ảnh #02) |
| Hệ số dự trữ thể tích thực tế | $f_s$ | $1.2$ | $\text{Không thứ nguyên}$ (Slide 10, 21, Ảnh #04) |
| Suất công suất khuấy trộn cơ học | $p_{\text{mix}}$ | $0.008$ | $\text{kW/m}^3$ (Slide 11, 21, Ảnh #04) |
| Suất lưu lượng không khí cấp | $q_{\text{air}}$ | $0.01$ | $\text{m}^3\text{ khí}/(\text{phút}\cdot\text{m}^3)$ (Slide 11, 21, Ảnh #04) |

**Bước 1 - Tính tổng thể tích nước thải ngày và lưu lượng trung bình giờ**: Cộng toàn bộ $24\text{ giá trị}$ lưu lượng giờ trên Slide 18 thu được $\sum V_{\text{in}} = 26,550\text{ m}^3\text{/ngày}$, từ đó tính được lưu lượng bơm ra ổn định $Q_{\text{avg}} = 1106.25\text{ m}^3\text{/h}$ [Page 9].

$$
Q_{\text{avg}} = \frac{\sum_{i=1}^{24} V_{\text{in},i}}{24} = \frac{26,550}{24} = 1106.25\text{ (m}^3\text{/h)}
$$

**Bước 2 - Lập bảng cân bằng thể tích tích lũy $24\text{ giờ}$ bắt đầu từ khung giờ N-13**: Theo đúng bảng chuẩn của thầy trên Slide 20 (Ảnh #03), tính chênh lệch thể tích từng giờ $\Delta V_i = V_{\text{in},i} - 1106.25$ để xác định cực đại $\max(\sum \Delta V) = +2691.00\text{ m}^3$ tại $23\text{–M}$ và cực tiểu $\min(\sum \Delta V) = -1407.00\text{ m}^3$ tại $7\text{–}8$ [Page 9].

$$
\Delta V_i = V_{\text{in},i} - V_{\text{out}}, \quad \sum \Delta V_k = \sum_{i=1}^{k} \left(V_{\text{in},i} - 1106.25\right)
$$

| Khung giờ | Lưu lượng vào $Q_{\text{in}}$ ($\text{m}^3\text{/h}$) | Thể tích vào $V_{\text{in}}$ ($\text{m}^3$) | Thể tích bơm ra $V_{\text{out}}$ ($\text{m}^3$) | Lượng tích trữ $\Delta V$ ($\text{m}^3$) | Thể tích tích lũy $\sum \Delta V$ ($\text{m}^3$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\text{N–13}$ | $1530$ | $1530.00$ | $1106.25$ | $+423.75$ | $+423.75$ |
| $13\text{–}14$ | $1458$ | $1458.00$ | $1106.25$ | $+351.75$ | $+775.50$ |
| $14\text{–}15$ | $1386$ | $1386.00$ | $1106.25$ | $+279.75$ | $+1055.25$ |
| $15\text{–}16$ | $1260$ | $1260.00$ | $1106.25$ | $+153.75$ | $+1209.00$ |
| $16\text{–}17$ | $1170$ | $1170.00$ | $1106.25$ | $+63.75$ | $+1272.75$ |
| $17\text{–}18$ | $1170$ | $1170.00$ | $1106.25$ | $+63.75$ | $+1336.50$ |
| $18\text{–}19$ | $1188$ | $1188.00$ | $1106.25$ | $+81.75$ | $+1418.25$ |
| $19\text{–}20$ | $1314$ | $1314.00$ | $1106.25$ | $+207.75$ | $+1626.00$ |
| $20\text{–}21$ | $1440$ | $1440.00$ | $1106.25$ | $+333.75$ | $+1959.75$ |
| $21\text{–}22$ | $1440$ | $1440.00$ | $1106.25$ | $+333.75$ | $+2293.50$ |
| $22\text{–}23$ | $1368$ | $1368.00$ | $1106.25$ | $+261.75$ | $+2555.25$ |
| $\mathbf{23\text{–M (Max)}}$ | $\mathbf{1242}$ | $\mathbf{1242.00}$ | $\mathbf{1106.25}$ | $\mathbf{+135.75}$ | $\mathbf{+2691.00}$ |
| $\text{M–1}$ | $990$ | $990.00$ | $1106.25$ | $-116.25$ | $+2574.75$ |
| $1\text{–}2$ | $792$ | $792.00$ | $1106.25$ | $-314.25$ | $+2260.50$ |
| $2\text{–}3$ | $594$ | $594.00$ | $1106.25$ | $-512.25$ | $+1748.25$ |
| $3\text{–}4$ | $468$ | $468.00$ | $1106.25$ | $-638.25$ | $+1110.00$ |
| $4\text{–}5$ | $378$ | $378.00$ | $1106.25$ | $-728.25$ | $+381.75$ |
| $5\text{–}6$ | $360$ | $360.00$ | $1106.25$ | $-746.25$ | $-364.50$ |
| $6\text{–}7$ | $432$ | $432.00$ | $1106.25$ | $-674.25$ | $-1038.75$ |
| $\mathbf{7\text{–8 (Min)}}$ | $\mathbf{738}$ | $\mathbf{738.00}$ | $\mathbf{1106.25}$ | $\mathbf{-368.25}$ | $\mathbf{-1407.00}$ |
| $8\text{–}9$ | $1278$ | $1278.00$ | $1106.25$ | $+171.75$ | $-1235.25$ |
| $9\text{–}10$ | $1476$ | $1476.00$ | $1106.25$ | $+369.75$ | $-865.50$ |
| $10\text{–}11$ | $1530$ | $1530.00$ | $1106.25$ | $+423.75$ | $-441.75$ |
| $11\text{–N}$ | $1548$ | $1548.00$ | $1106.25$ | $+441.75$ | $0.00$ |

**Bước 3 - Xác định thể tích bể điều hòa lý thuyết và thể tích thực tế**: Lấy hiệu số giữa giá trị tích lũy cực đại và cực tiểu trên Slide 21 (Ảnh #04) để tìm $V_{\text{theo}} = 4098\text{ m}^3$, sau đó nhân với hệ số $1.2$ thu được $V_{\text{prac}} = 4918\text{ m}^3$ [Page 5] [Page 9].

$$
V_{\text{theo}} = \max\left(\sum \Delta V\right) - \min\left(\sum \Delta V\right) = 2691 - (-1407) = 4098\text{ (m}^3\text{)}
$$

$$
V_{\text{prac}} = 1.2 \times V_{\text{theo}} = 1.2 \times 4098 = 4917.6\text{ m}^3 \approx 4918\text{ (m}^3\text{)}
$$

**Bước 4 - Tính công suất khuấy trộn cơ học và lưu lượng không khí cần cấp**: Nhân thể tích thực tế $V_{\text{prac}} = 4918\text{ m}^3$ với suất khuấy trộn $0.008\text{ kW/m}^3$ và suất cấp khí $0.01\text{ m}^3\text{/(phút}\cdot\text{m}^3\text{)}$ trên Slide 21, thu được $P_{\text{mix}} = 39\text{ kW}$ và $Q_{\text{air}} = 49\text{ m}^3\text{ khí/phút}$ [Page 6] [Page 9].

$$
P_{\text{mix}} = V_{\text{prac}} \times p_{\text{mix}} = 4918 \times 0.008 = 39.34\text{ kW} \approx 39\text{ (kW)}
$$

$$
Q_{\text{air}} = V_{\text{prac}} \times q_{\text{air}} = 4918 \times 0.01 = 49.18\text{ m}^3\text{/phút} \approx 49\text{ (m}^3\text{ khí/phút)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Lưu lượng bơm ra trung bình ($Q_{\text{avg}}$)**: $1106.25\text{ m}^3\text{/h}$ (Kiểm tra: $\sum \Delta V_{11\text{–N}} = -441.75 + 441.75 = 0.00\text{ m}^3\text{ — Đạt chuẩn Slide 20}$)
- **Thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$)**: $4098\text{ m}^3$ (Kiểm tra: $2691 - (-1407) = 4098\text{ m}^3\text{ — Đạt chuẩn Slide 20, 21}$)
- **Thể tích bể điều hòa thực tế ($V_{\text{prac}}$)**: $4918\text{ m}^3$ (Kiểm tra: $\frac{V_{\text{prac}}}{V_{\text{theo}}} = 1.2 \in [1.1, 1.2]\text{ — Đạt chuẩn Slide 10, 21}$)
- **Công suất khuấy trộn cơ học ($P_{\text{mix}}$)**: $39\text{ kW}$ (Kiểm tra: $p_{\text{mix}} = 0.008\text{ kW/m}^3 \in [0.004, 0.008]\text{ kW/m}^3\text{ — Đạt chuẩn Slide 11, 21}$)
- **Lưu lượng không khí cấp ($Q_{\text{air}}$)**: $49\text{ m}^3\text{ khí/phút}$ (Kiểm tra: $q_{\text{air}} = 0.01\text{ m}^3\text{/(phút}\cdot\text{m}^3\text{)} \in [0.01, 0.015]\text{ — Đạt chuẩn Slide 11, 21}$)

### Bài tập ch02_ex02 (Slide 25 đến 32 - Example 2): Tính toán cân bằng khối lượng và hiệu quả điều hòa nồng độ BOD

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy] kết hợp [Lời giải khôi phục theo chuẩn slide của thầy]): Sử dụng cùng bảng lưu lượng $24\text{ giờ}$ của Example 1 ($Q_{\text{out}} = 1106.25\text{ m}^3\text{/h}$, $V_{\text{theo}} = 4098\text{ m}^3$) kết hợp dữ liệu nồng độ $\text{BOD}$ đầu vào trên Slide 25 biến thiên từ $\text{BOD}_{\min} = 45\text{ mg/L}$ (khung giờ $4\text{–}5$) đến $\text{BOD}_{\max} = 305\text{ mg/L}$ (khung giờ $21\text{–}22$), hãy lập bảng cân bằng chất $24\text{ giờ}$ để xác định nồng độ $\text{BOD}_{\text{eq}}$ và tải lượng $\text{BOD}$ sau điều hòa [Page 9].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng bơm ra cố định mỗi giờ | $V_{\text{out}}$ | $1106.25$ | $\text{m}^3\text{/h}$ (Slide 26, Ảnh #07) |
| Nồng độ $\text{BOD}$ đầu vào trung bình | $\text{BOD}_{\text{avg}}$ | $170$ | $\text{mg/L}$ (Slide 26, 32, Ảnh #07, #09) |
| Tải lượng khối $\text{BOD}$ trung bình giờ | $L_{\text{avg}}$ | $213$ | $\text{kg/h}$ (Slide 26, 32, Ảnh #07, #10) |
| Thể tích nước tồn trong bể cuối giờ $7\text{–}8$ | $V_{sp,8\text{–}9}$ | $0.00$ | $\text{m}^3$ (Slide 26, 27, Ảnh #07, #08) |

**Bước 1 - Thiết lập phương trình cân bằng khối lượng nồng độ $\text{BOD}$ hoàn toàn xáo trộn**: Theo Slide 26 (Ảnh #07), nồng độ $\text{BOD}$ sau điều hòa ở mỗi giờ bằng tổng khối lượng $\text{BOD}$ dòng vào cộng khối lượng $\text{BOD}$ tồn đầu giờ chia cho tổng thể tích nước trong bể [Page 9].

$$
\text{BOD}_{\text{eq}} = \frac{V_{ic} \cdot \text{BOD}_{ic} + V_{sp} \cdot \text{BOD}_{sp}}{V_{ic} + V_{sp}}
$$

$$
V_{\text{end}} = V_{sp} + V_{ic} - V_{\text{out}} = V_{sp} + V_{ic} - 1106.25
$$

**Bước 2 - Tính mẫu bốn khung giờ đầu tiên từ $8\text{–}9$ đến $11\text{–N}$ theo Slide 27**: Bắt đầu tại khung giờ $8\text{–}9$ khi bể vừa cạn ($V_{sp} = 0\text{ m}^3$), áp dụng phân số cân bằng khối lượng trên Slide 27 (Ảnh #08) thu được $\text{BOD}_{\text{eq}}$ lần lượt bằng $175$, $197$, $210$ và $216\text{ mg/L}$ [Page 9].

$$
\text{BOD}_{\text{eq},8\text{–}9} = \frac{1278 \times 175 + 0 \times 0}{1278 + 0} = 175\text{ (mg/L)}, \quad V_{\text{end},8\text{–}9} = 171.75\text{ (m}^3\text{)}
$$

$$
\text{BOD}_{\text{eq},9\text{–}10} = \frac{1476 \times 200 + 171.75 \times 175}{1476 + 171.75} = 197.39 \approx 197\text{ (mg/L)}
$$

$$
\text{BOD}_{\text{eq},10\text{–}11} = \frac{1530 \times 215 + 541.50 \times 197.39}{1530 + 541.50} = 210.40 \approx 210\text{ (mg/L)}
$$

$$
\text{BOD}_{\text{eq},11\text{–N}} = \frac{1548 \times 220 + 965.25 \times 210.40}{1548 + 965.25} = 216.31 \approx 216\text{ (mg/L)}
$$

**Bước 3 - Lập bảng cân bằng chất $24\text{ giờ}$ và tính tải lượng $\text{BOD}$ trước, sau điều hòa**: Tính liên tiếp từ khung giờ $8\text{–}9$ đến $7\text{–}8$ hôm sau và đổi tải lượng khối sang $\text{kg/h}$ bằng cách chia cho $1000\text{ g/kg}$, xác định được đỉnh $\text{BOD}_{\text{eq},\max} = 246\text{ mg/L}$ tại $21\text{–}22$ và đáy $\text{BOD}_{\text{eq},\min} = 121\text{ mg/L}$ tại $6\text{–}7$ [Page 9].

$$
L_{\text{trước}} = \frac{V_{ic} \cdot \text{BOD}_{ic}}{1000}\text{ (kg/h)}, \quad L_{\text{sau}} = \frac{1106.25 \cdot \text{BOD}_{\text{eq}}}{1000}\text{ (kg/h)}
$$

| Khung giờ | Thể tích vào $V_{ic}$ ($\text{m}^3$) | Tồn đầu giờ $V_{sp}$ ($\text{m}^3$) | Tồn cuối giờ $V_{\text{end}}$ ($\text{m}^3$) | $\text{BOD}$ vào $\text{BOD}_{ic}$ ($\text{mg/L}$) | $\text{BOD}$ ra $\text{BOD}_{\text{eq}}$ ($\text{mg/L}$) | Tải lượng trước / sau ($\text{kg/h}$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $8\text{–}9$ | $1278.00$ | $0.00$ | $171.75$ | $175$ | $175$ | $224$ / $194$ |
| $9\text{–}10$ | $1476.00$ | $171.75$ | $541.50$ | $200$ | $197$ | $295$ / $218$ |
| $10\text{–}11$ | $1530.00$ | $541.50$ | $965.25$ | $215$ | $210$ | $329$ / $232$ |
| $11\text{–N}$ | $1548.00$ | $965.25$ | $1407.00$ | $220$ | $216$ | $341$ / $239$ |
| $\text{N–13}$ | $1530.00$ | $1407.00$ | $1830.75$ | $220$ | $218$ | $337$ / $241$ |
| $13\text{–}14$ | $1458.00$ | $1830.75$ | $2182.50$ | $210$ | $215$ | $306$ / $238$ |
| $14\text{–}15$ | $1386.00$ | $2182.50$ | $2462.25$ | $200$ | $209$ | $277$ / $231$ |
| $15\text{–}16$ | $1260.00$ | $2462.25$ | $2616.00$ | $190$ | $203$ | $239$ / $225$ |
| $16\text{–}17$ | $1170.00$ | $2616.00$ | $2679.75$ | $180$ | $196$ | $211$ / $217$ |
| $17\text{–}18$ | $1170.00$ | $2679.75$ | $2743.50$ | $170$ | $188$ | $199$ / $208$ |
| $18\text{–}19$ | $1188.00$ | $2743.50$ | $2825.25$ | $175$ | $184$ | $208$ / $204$ |
| $19\text{–}20$ | $1314.00$ | $2825.25$ | $3033.00$ | $210$ | $192$ | $276$ / $212$ |
| $20\text{–}21$ | $1440.00$ | $3033.00$ | $3366.75$ | $280$ | $220$ | $403$ / $243$ |
| $\mathbf{21\text{–22 (Max)}}$ | $\mathbf{1440.00}$ | $\mathbf{3366.75}$ | $\mathbf{3700.50}$ | $\mathbf{305}$ | $\mathbf{246}$ | $\mathbf{439}$ / $\mathbf{272}$ |
| $22\text{–}23$ | $1368.00$ | $3700.50$ | $3962.25$ | $245$ | $246$ | $335$ / $272$ |
| $23\text{–M}$ | $1242.00$ | $3962.25$ | $4098.00$ | $180$ | $230$ | $224$ / $254$ |
| $\text{M–1}$ | $990.00$ | $4098.00$ | $3981.75$ | $150$ | $214$ | $148$ / $237$ |
| $1\text{–}2$ | $792.00$ | $3981.75$ | $3667.50$ | $115$ | $198$ | $91$ / $219$ |
| $2\text{–}3$ | $594.00$ | $3667.50$ | $3155.25$ | $75$ | $181$ | $45$ / $200$ |
| $3\text{–}4$ | $468.00$ | $3155.25$ | $2517.00$ | $50$ | $164$ | $23$ / $181$ |
| $\mathbf{4\text{–5 (Min in)}}$ | $\mathbf{378.00}$ | $\mathbf{2517.00}$ | $\mathbf{1788.75}$ | $\mathbf{45}$ | $\mathbf{148}$ | $\mathbf{17}$ / $\mathbf{164}$ |
| $5\text{–}6$ | $360.00$ | $1788.75$ | $1042.50$ | $60$ | $134$ | $22$ / $148$ |
| $\mathbf{6\text{–7 (Min eq)}}$ | $\mathbf{432.00}$ | $\mathbf{1042.50}$ | $\mathbf{368.25}$ | $\mathbf{90}$ | $\mathbf{121}$ | $\mathbf{39}$ / $\mathbf{134}$ |
| $7\text{–}8$ | $738.00$ | $368.25$ | $0.00$ | $130$ | $127$ | $96$ / $140$ |

**Bước 4 - Đánh giá tỷ số cực đại, cực tiểu của nồng độ và tải lượng $\text{BOD}$ theo Slide 32**: So sánh hai bảng tổng hợp trên Slide 32 (Ảnh #09 và #10), tỷ số $\text{Peak/Min}$ của nồng độ giảm từ $6.78$ xuống $2.03$ và tỷ số $\text{Peak/Min}$ của tải lượng khối giảm hơn $12\text{ lần}$ từ $25.82$ xuống $2.03$ [Page 9].

$$
\left(\frac{\text{Peak}}{\text{Min}}\right)_{\text{BOD}} = \frac{305}{45} = 6.78 \implies \left(\frac{\text{Peak}}{\text{Min}}\right)_{\text{BOD,eq}} = \frac{246}{121} = 2.03
$$

$$
\left(\frac{\text{Peak}}{\text{Min}}\right)_{\text{Load}} = \frac{439}{17} = 25.82 \implies \left(\frac{\text{Peak}}{\text{Min}}\right)_{\text{Load,eq}} = \frac{272}{134} = 2.03
$$

| Chỉ tiêu đánh giá (Slide 32) | Đơn vị | Trước điều hòa | Sau điều hòa | Tỷ số $\frac{\text{Peak}}{\text{Average}}$ (Trước / Sau) | Tỷ số $\frac{\text{Min}}{\text{Average}}$ (Trước / Sau) | Tỷ số $\frac{\text{Peak}}{\text{Min}}$ (Trước / Sau) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Nồng độ $\text{BOD}$ cực đại ($\text{Peak}$) | $\text{mg/L}$ | $305$ | $246$ | $1.79$ / $1.45$ | $0.26$ / $0.71$ | $6.78$ / $2.03$ |
| Nồng độ $\text{BOD}$ cực tiểu ($\text{Min}$) | $\text{mg/L}$ | $45$ | $121$ | $1.79$ / $1.45$ | $0.26$ / $0.71$ | $6.78$ / $2.03$ |
| Tải lượng $\text{BOD}$ cực đại ($\text{Peak}$) | $\text{kg/h}$ | $439$ | $272$ | $2.06$ / $1.28$ | $0.08$ / $0.63$ | $25.82$ / $2.03$ |
| Tải lượng $\text{BOD}$ cực tiểu ($\text{Min}$) | $\text{kg/h}$ | $17$ | $134$ | $2.06$ / $1.28$ | $0.08$ / $0.63$ | $25.82$ / $2.03$ |

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Nồng độ $\text{BOD}$ cực đại sau điều hòa ($\text{BOD}_{\text{eq},\max}$)**: $246\text{ mg/L}$ (Kiểm tra: $246\text{ mg/L} < 305\text{ mg/L}\text{ tại giờ } 21\text{–}22\text{ — Đạt chuẩn Slide 32}$)
- **Nồng độ $\text{BOD}$ cực tiểu sau điều hòa ($\text{BOD}_{\text{eq},\min}$)**: $121\text{ mg/L}$ (Kiểm tra: $121\text{ mg/L} > 45\text{ mg/L}\text{ tại giờ } 6\text{–}7\text{ — Đạt chuẩn Slide 32}$)
- **Tỷ số $\text{Peak/Min}$ của nồng độ $\text{BOD}$**: $2.03$ (Kiểm tra: $\frac{246}{121} = 2.03 < \frac{305}{45} = 6.78\text{ — Đạt chuẩn Slide 32}$)
- **Tỷ số $\text{Peak/Min}$ của tải lượng $\text{BOD}$**: $2.03$ (Kiểm tra: $\frac{272}{134} = 2.03 \ll \frac{439}{17} = 25.82\text{ — Đạt chuẩn Slide 32}$)

### Bài tập proj_ch02_hw01 (Slide 33 đến 38 - Homework trên lớp): Thiết kế bể điều hòa cho nhà máy làm việc 2 ca

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy]): Một nhà máy hoạt động $2\text{ ca/ngày}$, mỗi ca kéo dài $8\text{ giờ}$ với quy mô $N = 1000\text{ công nhân/ca}$ [Page 5]. Tiêu chuẩn dùng nước sinh hoạt cho công nhân là $q_w = 45\text{ L/(người}\cdot\text{ca)}$ phân bố đều trong $8\text{ giờ}$ làm việc, và cuối mỗi ca nhà máy sử dụng thêm $V_c = 3\text{ m}^3\text{/ca}$ nước để vệ sinh nhà xưởng và thiết bị [Page 5]. Giả sử lưu lượng nước thải bằng $100\%$ lưu lượng nước cấp, hãy xác định công suất trạm xử lý nước thải ($Q_{\text{plant}}$), thể tích bể điều hòa thực tế ($V_{\text{prac}}$) và lưu lượng không khí cần cấp ($Q_{\text{air}}$) [Page 5] [Page 6].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Số ca làm việc và thời gian mỗi ca | $n_{\text{ca}}, t_{\text{ca}}$ | $2, 8$ | $\text{ca/ngày}, \text{giờ/ca}$ (Slide 33, Ảnh #11) |
| Số lượng công nhân làm việc mỗi ca | $N$ | $1000$ | $\text{người/ca}$ (Slide 33, Ảnh #11) |
| Tiêu chuẩn cấp nước sinh hoạt công nhân | $q_w$ | $45$ | $\text{L/(người}\cdot\text{ca)}$ (Slide 33, Ảnh #11) |
| Lượng nước vệ sinh nhà xưởng cuối mỗi ca | $V_c$ | $3$ | $\text{m}^3\text{/ca}$ (Slide 33, Ảnh #11) |
| Hệ số dự trữ thể tích và suất cấp khí | $f_s, q_{\text{air}}$ | $1.2, 0.012$ | $\text{Không thứ nguyên}, \text{m}^3\text{/(phút}\cdot\text{m}^3\text{)}$ (Ảnh #16, #17) |

**Bước 1 - Xác định công suất trạm xử lý nước thải của nhà máy làm việc $2\text{ ca}$**: Theo Slide 34 (Ảnh #14), cộng tổng lượng nước cấp cho công nhân trong $2\text{ ca}$ ($90\text{ m}^3\text{/ngày}$) và lượng nước rửa xưởng cuối $2\text{ ca}$ ($6\text{ m}^3\text{/ngày}$), thu được công suất trạm $Q_{\text{plant}} = 96\text{ m}^3\text{/ngày}$ [Page 5].

$$
Q_{\text{worker}} = 2 \times 1000 \times 45 \times \frac{1\text{ m}^3}{1000\text{ L}} = 90\text{ (m}^3\text{/ngày)}
$$

$$
Q_{\text{plant}} = Q_{\text{worker}} + 2 \times V_c = 90 + 2 \times 3 = 96\text{ (m}^3\text{/ngày)}
$$

**Bước 2 - Tính lưu lượng vào từng giờ làm việc và lưu lượng bơm ra trung bình**: Chia đều công suất $96\text{ m}^3\text{/ngày}$ cho $24\text{ giờ}$ được lưu lượng bơm ra $V_{\text{out}} = 4\text{ m}^3\text{/h}$, trong khi lưu lượng vào ở các giờ làm việc bình thường là $5.625\text{ m}^3\text{/h}$ và ở giờ cuối mỗi ca (giờ $8$ và giờ $16$) là $8.625\text{ m}^3\text{/h}$ [Page 5].

$$
V_{\text{out}} = \frac{Q_{\text{plant}}}{24} = \frac{96}{24} = 4.000\text{ (m}^3\text{/h)}
$$

$$
V_{\text{in, giờ thường}} = \frac{45\text{ m}^3}{8\text{ h}} = 5.625\text{ (m}^3\text{/h)}, \quad V_{\text{in, cuối ca}} = 5.625 + 3.000 = 8.625\text{ (m}^3\text{/h)}
$$

**Bước 3 - Lập bảng tích lũy thể tích $24\text{ giờ}$ và tính thể tích bể điều hòa thực tế**: Theo bảng tính trên Slide 35 và 36 (Ảnh #15 và #16), thể tích tích lũy đạt cực đại $\max(\sum \Delta V) = 32.000\text{ m}^3$ ở cuối giờ $16$ và giảm về cực tiểu $\min(\sum \Delta V) = 0.000\text{ m}^3$ ở giờ $24$, cho $V_{\text{theo}} = 32\text{ m}^3$ và $V_{\text{prac}} = 38.4\text{ m}^3$ [Page 5].

$$
V_{\text{theo}} = 32.000 - 0.000 = 32\text{ (m}^3\text{)}, \quad V_{\text{prac}} = 1.2 \times 32 = 38.4\text{ (m}^3\text{)}
$$

| Giờ thứ | Ca hoạt động | Thể tích vào $V_{\text{in}}$ ($\text{m}^3$) | Thể tích ra $V_{\text{out}}$ ($\text{m}^3$) | Tích trữ $\Delta V$ ($\text{m}^3$) | Thể tích tích lũy $\sum \Delta V$ ($\text{m}^3$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\text{Giờ } 1$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+1.625$ |
| $\text{Giờ } 2$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+3.250$ |
| $\text{Giờ } 3$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+4.875$ |
| $\text{Giờ } 4$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+6.500$ |
| $\text{Giờ } 5$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+8.125$ |
| $\text{Giờ } 6$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+9.750$ |
| $\text{Giờ } 7$ | $\text{Ca } 1$ | $5.625$ | $4.000$ | $+1.625$ | $+11.375$ |
| $\text{Giờ } 8$ | $\text{Cuối Ca } 1$ | $8.625$ | $4.000$ | $+4.625$ | $+16.000$ |
| $\text{Giờ } 9$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+17.625$ |
| $\text{Giờ } 10$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+19.250$ |
| $\text{Giờ } 11$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+20.875$ |
| $\text{Giờ } 12$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+22.500$ |
| $\text{Giờ } 13$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+24.125$ |
| $\text{Giờ } 14$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+25.750$ |
| $\text{Giờ } 15$ | $\text{Ca } 2$ | $5.625$ | $4.000$ | $+1.625$ | $+27.375$ |
| $\mathbf{\text{Giờ } 16\text{ (Max)}}$ | $\mathbf{\text{Cuối Ca } 2}$ | $\mathbf{8.625}$ | $\mathbf{4.000}$ | $\mathbf{+4.625}$ | $\mathbf{+32.000}$ |
| $\text{Giờ } 17$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+28.000$ |
| $\text{Giờ } 18$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+24.000$ |
| $\text{Giờ } 19$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+20.000$ |
| $\text{Giờ } 20$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+16.000$ |
| $\text{Giờ } 21$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+12.000$ |
| $\text{Giờ } 22$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+8.000$ |
| $\text{Giờ } 23$ | $\text{Nghỉ đêm}$ | $0.000$ | $4.000$ | $-4.000$ | $+4.000$ |
| $\mathbf{\text{Giờ } 24\text{ (Min)}}$ | $\mathbf{\text{Nghỉ đêm}}$ | $\mathbf{0.000}$ | $\mathbf{4.000}$ | $\mathbf{-4.000}$ | $\mathbf{0.000}$ |

**Bước 4 - Tính lưu lượng không khí cần cấp cho bể điều hòa**: Theo Slide 37 (Ảnh #17), chọn suất cấp khí $q_{\text{air}} = 0.012\text{ m}^3\text{ khí}/(\text{phút}\cdot\text{m}^3)$ nhân với thể tích thực tế $V_{\text{prac}} = 38.4\text{ m}^3$, thu được $Q_{\text{air}} = 0.46\text{ m}^3\text{/phút}$ [Page 6].

$$
Q_{\text{air}} = q_{\text{air}} \times V_{\text{prac}} = 0.012 \times 38.4 = 0.4608\text{ m}^3\text{/phút} \approx 0.46\text{ (m}^3\text{ khí/phút)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Công suất trạm xử lý nước thải ($Q_{\text{plant}}$)**: $96\text{ m}^3\text{/ngày}$ (Kiểm tra: $Q_{\text{out}} = \frac{96}{24} = 4.000\text{ m}^3\text{/h}\text{ — Đạt chuẩn Ảnh \#14, \#15}$)
- **Thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$)**: $32\text{ m}^3$ (Kiểm tra: $\sum \Delta V_{16} - \sum \Delta V_{24} = 32 - 0 = 32\text{ m}^3\text{ — Đạt chuẩn Ảnh \#16}$)
- **Thể tích bể điều hòa thực tế ($V_{\text{prac}}$)**: $38.4\text{ m}^3$ (Kiểm tra: $32 \times 120\% = 38.4\text{ m}^3\text{ — Đạt chuẩn Ảnh \#16}$)
- **Lưu lượng không khí cấp ($Q_{\text{air}}$)**: $0.46\text{ m}^3\text{/phút}$ (Kiểm tra: $q_{\text{air}} = 0.012 \in [0.01, 0.015]\text{ m}^3\text{/(phút}\cdot\text{m}^3\text{) — Đạt chuẩn Ảnh \#17}$)

### Bài tập proj_ch02_ex01 (Slide 39 - Exercise 1 trên lớp): Ước tính thể tích bể điều hòa cho trạm xử lý nước thải thành phố

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Ước tính thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$), thể tích bể điều hòa thực tế ($V_{\text{prac}}$), công suất khuấy trộn ($P_{\text{mix}}$) và lưu lượng khí cấp ($Q_{\text{air}}$) cho một thành phố có bảng lưu lượng nước thải trong $24\text{ giờ}$ trên Slide 39 (Ảnh #12) cho theo đơn vị $\text{m}^3\text{/s}$ từ $Q_{\min} = 0.160\text{ m}^3\text{/s}$ (khung giờ $3\text{–}5$) đến $Q_{\max} = 0.480\text{ m}^3\text{/s}$ (khung giờ $10\text{–N}$) [Page 5] [Page 6].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Hệ số quy đổi thời gian từ giây sang giờ | $k_t$ | $3600$ | $\text{s/h}$ (Slide 39, Ảnh #12) |
| Tổng thể tích nước thải thành phố trong ngày | $\sum V_{\text{in}}$ | $28,371.60$ | $\text{m}^3\text{/ngày}$ (Tính từ Slide 39) |
| Lưu lượng bơm ra trung bình mỗi giờ | $Q_{\text{avg}}$ | $1182.15$ | $\text{m}^3\text{/h}$ (Ứng với $0.328375\text{ m}^3\text{/s}$) |
| Hệ số dự trữ thể tích thực tế | $f_s$ | $1.2$ | $\text{Không thứ nguyên}$ (Slide 10) |
| Suất công suất khuấy trộn và suất cấp khí | $p_{\text{mix}}, q_{\text{air}}$ | $0.008, 0.01$ | $\text{kW/m}^3, \text{m}^3\text{/(phút}\cdot\text{m}^3\text{)}$ (Slide 11) |

**Bước 1 - Quy đổi lưu lượng sang $\text{m}^3\text{/h}$ và tính lưu lượng trung bình ngày**: Nhân lưu lượng $Q_{\text{in}}$ ($\text{m}^3\text{/s}$) của từng giờ với $3600\text{ s/h}$ thu được tổng thể tích ngày $\sum V_{\text{in}} = 28,371.60\text{ m}^3\text{/ngày}$ và lưu lượng bơm ra trung bình $V_{\text{out}} = 1182.15\text{ m}^3\text{/h}$ [Page 5].

$$
V_{\text{in},i} = Q_{\text{in},i} \times 3600\text{ (m}^3\text{/h)}, \quad V_{\text{out}} = \frac{\sum_{i=1}^{24} V_{\text{in},i}}{24} = \frac{28,371.60}{24} = 1182.15\text{ (m}^3\text{/h)}
$$

**Bước 2 - Lập bảng cân bằng thể tích tích lũy $24\text{ giờ}$ của thành phố**: Tính lượng tích trữ mỗi giờ $\Delta V_i = V_{\text{in},i} - 1182.15$ từ khung giờ $\text{M–1}$ đến $23\text{–M}$, xác định được cực tiểu $\min(\sum \Delta V) = -3175.20\text{ m}^3$ tại $7\text{–}8$ và cực đại $\max(\sum \Delta V) = +102.15\text{ m}^3$ tại $22\text{–}23$ [Page 5].

$$
\Delta V_i = V_{\text{in},i} - 1182.15, \quad \sum \Delta V_k = \sum_{i=1}^{k} \Delta V_i
$$

| Khung giờ | Lưu lượng $Q_{\text{in}}$ ($\text{m}^3\text{/s}$) | Thể tích vào $V_{\text{in}}$ ($\text{m}^3$) | Thể tích ra $V_{\text{out}}$ ($\text{m}^3$) | Tích trữ $\Delta V$ ($\text{m}^3$) | Thể tích tích lũy $\sum \Delta V$ ($\text{m}^3$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\text{M–1}$ | $0.300$ | $1080.00$ | $1182.15$ | $-102.15$ | $-102.15$ |
| $1\text{–}2$ | $0.220$ | $792.00$ | $1182.15$ | $-390.15$ | $-492.30$ |
| $2\text{–}3$ | $0.180$ | $648.00$ | $1182.15$ | $-534.15$ | $-1026.45$ |
| $3\text{–}4$ | $0.160$ | $576.00$ | $1182.15$ | $-606.15$ | $-1632.60$ |
| $4\text{–}5$ | $0.160$ | $576.00$ | $1182.15$ | $-606.15$ | $-2238.75$ |
| $5\text{–}6$ | $0.185$ | $666.00$ | $1182.15$ | $-516.15$ | $-2754.90$ |
| $6\text{–}7$ | $0.240$ | $864.00$ | $1182.15$ | $-318.15$ | $-3073.05$ |
| $\mathbf{7\text{–8 (Min)}}$ | $\mathbf{0.300}$ | $\mathbf{1080.00}$ | $\mathbf{1182.15}$ | $\mathbf{-102.15}$ | $\mathbf{-3175.20}$ |
| $8\text{–}9$ | $0.385$ | $1386.00$ | $1182.15$ | $+203.85$ | $-2971.35$ |
| $9\text{–}10$ | $0.440$ | $1584.00$ | $1182.15$ | $+401.85$ | $-2569.50$ |
| $10\text{–}11$ | $0.480$ | $1728.00$ | $1182.15$ | $+545.85$ | $-2023.65$ |
| $11\text{–N}$ | $0.480$ | $1728.00$ | $1182.15$ | $+545.85$ | $-1477.80$ |
| $\text{N–13}$ | $0.460$ | $1656.00$ | $1182.15$ | $+473.85$ | $-1003.95$ |
| $13\text{–}14$ | $0.420$ | $1512.00$ | $1182.15$ | $+329.85$ | $-674.10$ |
| $14\text{–}15$ | $0.390$ | $1404.00$ | $1182.15$ | $+221.85$ | $-452.25$ |
| $15\text{–}16$ | $0.355$ | $1278.00$ | $1182.15$ | $+95.85$ | $-356.40$ |
| $16\text{–}17$ | $0.331$ | $1191.60$ | $1182.15$ | $+9.45$ | $-346.95$ |
| $17\text{–}18$ | $0.315$ | $1134.00$ | $1182.15$ | $-48.15$ | $-395.10$ |
| $18\text{–}19$ | $0.320$ | $1152.00$ | $1182.15$ | $-30.15$ | $-425.25$ |
| $19\text{–}20$ | $0.346$ | $1245.60$ | $1182.15$ | $+63.45$ | $-361.80$ |
| $20\text{–}21$ | $0.362$ | $1303.20$ | $1182.15$ | $+121.05$ | $-240.75$ |
| $21\text{–}22$ | $0.392$ | $1411.20$ | $1182.15$ | $+229.05$ | $-11.70$ |
| $\mathbf{22\text{–23 (Max)}}$ | $\mathbf{0.360}$ | $\mathbf{1296.00}$ | $\mathbf{1182.15}$ | $\mathbf{+113.85}$ | $\mathbf{+102.15}$ |
| $23\text{–M}$ | $0.300$ | $1080.00$ | $1182.15$ | $-102.15$ | $0.00$ |

**Bước 3 - Xác định thể tích bể điều hòa lý thuyết và thực tế**: Lấy hiệu số giữa cực đại $+102.15\text{ m}^3$ và cực tiểu $-3175.20\text{ m}^3$ thu được $V_{\text{theo}} = 3277.35\text{ m}^3$, sau đó nhân với hệ số an toàn $1.2$ thu được $V_{\text{prac}} = 3932.82\text{ m}^3$ [Page 5].

$$
V_{\text{theo}} = \max\left(\sum \Delta V\right) - \min\left(\sum \Delta V\right) = 102.15 - (-3175.20) = 3277.35\text{ (m}^3\text{)}
$$

$$
V_{\text{prac}} = 1.2 \times V_{\text{theo}} = 1.2 \times 3277.35 = 3932.82\text{ (m}^3\text{)} \approx 3933\text{ (m}^3\text{)}
$$

**Bước 4 - Tính công suất khuấy trộn và lưu lượng không khí cấp cho bể**: Nhân thể tích thực tế $V_{\text{prac}} = 3932.82\text{ m}^3$ với suất khuấy trộn $0.008\text{ kW/m}^3$ và suất cấp khí $0.01\text{ m}^3\text{/(phút}\cdot\text{m}^3\text{)}$, thu được $P_{\text{mix}} = 31.46\text{ kW}$ và $Q_{\text{air}} = 39.33\text{ m}^3\text{/phút}$ [Page 6].

$$
P_{\text{mix}} = 3932.82 \times 0.008 = 31.46\text{ (kW)}, \quad Q_{\text{air}} = 3932.82 \times 0.01 = 39.33\text{ (m}^3\text{ khí/phút)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Lưu lượng trung bình giờ ($Q_{\text{avg}}$)**: $1182.15\text{ m}^3\text{/h}$ (Kiểm tra: $\sum \Delta V_{23\text{–M}} = +102.15 - 102.15 = 0.00\text{ m}^3\text{ — Đạt chuẩn Slide 20}$)
- **Thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$)**: $3277.35\text{ m}^3$ (Kiểm tra: $102.15 - (-3175.20) = 3277.35\text{ m}^3\text{ — Đạt chuẩn Slide 9}$)
- **Thể tích bể điều hòa thực tế ($V_{\text{prac}}$)**: $3932.82\text{ m}^3$ (Kiểm tra: $\frac{V_{\text{prac}}}{V_{\text{theo}}} = 1.2 \in [1.1, 1.2]\text{ — Đạt chuẩn Slide 10}$)
- **Công suất khuấy trộn và lưu lượng khí ($P_{\text{mix}}, Q_{\text{air}}$)**: $31.46\text{ kW}, 39.33\text{ m}^3\text{/phút}$ (Kiểm tra: $p_{\text{mix}} = 0.008\text{ kW/m}^3, q_{\text{air}} = 0.01\text{ m}^3\text{/(phút}\cdot\text{m}^3\text{) — Đạt chuẩn Slide 11}$)

### Bài tập proj_ch02_ex02 (Slide 40 - Exercise 2 trên lớp): Xác định thể tích bể điều hòa và nồng độ BOD, TSS sau điều hòa theo chu kỳ 2 giờ

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Từ bảng số liệu đo đạc theo $12\text{ chu kỳ}$ (mỗi chu kỳ kéo dài $2\text{ giờ}$) trên Slide 40 (Ảnh #13) gồm thể tích nước thải vào $V_{ic}$ ($\text{m}^3$), nồng độ $\text{BOD}_{ic}$ ($\text{mg/L}$) và nồng độ $\text{TSS}_{ic}$ ($\text{mg/L}$), hãy xác định thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$), thể tích thực tế ($V_{\text{prac}}$), cùng biến thiên nồng độ $\text{BOD}_{\text{eq}}$ và $\text{TSS}_{\text{eq}}$ sau điều hòa [Page 5] [Page 9].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Số chu kỳ quan trắc và độ dài mỗi chu kỳ | $n_p, \Delta t$ | $12, 2$ | $\text{chu kỳ/ngày}, \text{giờ/chu kỳ}$ (Slide 40, Ảnh #13) |
| Tổng thể tích nước thải trong $24\text{ giờ}$ | $\sum V_{ic}$ | $1216.00$ | $\text{m}^3\text{/ngày}$ (Tính từ Slide 40) |
| Thể tích bơm ra ổn định mỗi chu kỳ $2\text{ giờ}$ | $V_{\text{out}}$ | $101.33$ | $\text{m}^3\text{/(2h)}$ (Ứng với $50.67\text{ m}^3\text{/h}$) |
| Hệ số dự trữ thể tích thực tế | $f_s$ | $1.2$ | $\text{Không thứ nguyên}$ (Slide 10) |
| Thể tích tồn trong bể cuối chu kỳ $4\text{–}6$ | $V_{sp,6\text{–}8}$ | $0.00$ | $\text{m}^3$ (Điểm cạn bể khởi đầu cân bằng chất) |

**Bước 1 - Tính tổng thể tích nước thải ngày và thể tích bơm ra mỗi chu kỳ $2\text{ giờ}$**: Cộng $12\text{ giá trị}$ thể tích dòng vào thu được $\sum V_{ic} = 1216\text{ m}^3\text{/ngày}$, suy ra thể tích bơm ra đều trong mỗi chu kỳ $2\text{ giờ}$ là $V_{\text{out}} = 101.33\text{ m}^3$ [Page 5].

$$
\sum_{i=1}^{12} V_{ic,i} = 80 + 60 + 94 + 128 + 130 + 144 + 120 + 96 + 110 + 80 + 90 + 84 = 1216\text{ (m}^3\text{/ngày)}
$$

$$
V_{\text{out}} = \frac{\sum_{i=1}^{12} V_{ic,i}}{12} = \frac{1216}{12} = 101.33\text{ (m}^3\text{/chu kỳ 2h)}
$$

**Bước 2 - Xác định thể tích bể điều hòa lý thuyết và thực tế từ cực trị tích lũy**: Lập cột tích lũy $\sum \Delta V$ từ $\text{M–2}$ đến $22\text{–M}$ tìm được cực tiểu $\min(\sum \Delta V) = -70.00\text{ m}^3$ tại $4\text{–}6$ và cực đại $\max(\sum \Delta V) = +50.00\text{ m}^3$ tại $16\text{–}18$, cho $V_{\text{theo}} = 120\text{ m}^3$ và $V_{\text{prac}} = 144\text{ m}^3$ [Page 5].

$$
V_{\text{theo}} = \max\left(\sum \Delta V\right) - \min\left(\sum \Delta V\right) = 50.00 - (-70.00) = 120.00\text{ (m}^3\text{)}
$$

$$
V_{\text{prac}} = 1.2 \times V_{\text{theo}} = 1.2 \times 120.00 = 144.00\text{ (m}^3\text{)}
$$

**Bước 3 - Lập bảng cân bằng thể tích và nồng độ $\text{BOD}$, $\text{TSS}$ sau điều hòa cho $12\text{ chu kỳ}$**: Bắt đầu tính cân bằng khối lượng tại chu kỳ $6\text{–}8$ (ngay sau khi bể cạn $V_{sp} = 0.00\text{ m}^3$ ở cuối chu kỳ $4\text{–}6$) cho cả hai chỉ tiêu $\text{BOD}$ và $\text{TSS}$ [Page 9].

$$
\text{BOD}_{\text{eq}} = \frac{V_{ic} \cdot \text{BOD}_{ic} + V_{sp} \cdot \text{BOD}_{sp}}{V_{ic} + V_{sp}}, \quad \text{TSS}_{\text{eq}} = \frac{V_{ic} \cdot \text{TSS}_{ic} + V_{sp} \cdot \text{TSS}_{sp}}{V_{ic} + V_{sp}}
$$

| Chu kỳ $2\text{ giờ}$ | Thể tích vào $V_{ic}$ ($\text{m}^3$) | Thể tích ra $V_{\text{out}}$ ($\text{m}^3$) | Tích lũy $\sum \Delta V$ ($\text{m}^3$) | Tồn đầu kỳ $V_{sp}$ ($\text{m}^3$) | Tồn cuối kỳ $V_{\text{end}}$ ($\text{m}^3$) | $\text{BOD}_{ic}$ / $\text{BOD}_{\text{eq}}$ ($\text{mg/L}$) | $\text{TSS}_{ic}$ / $\text{TSS}_{\text{eq}}$ ($\text{mg/L}$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $6\text{–}8$ | $128.00$ | $101.33$ | $-43.33$ | $0.00$ | $26.67$ | $220$ / $220$ | $205$ / $205$ |
| $8\text{–}10$ | $130.00$ | $101.33$ | $-14.67$ | $26.67$ | $55.33$ | $230$ / $228$ | $210$ / $209$ |
| $\mathbf{10\text{–N (Max } C_{\text{eq}}\mathbf{)}}$ | $\mathbf{144.00}$ | $\mathbf{101.33}$ | $\mathbf{+28.00}$ | $\mathbf{55.33}$ | $\mathbf{98.00}$ | $\mathbf{245}$ / $\mathbf{240}$ | $\mathbf{220}$ / $\mathbf{217}$ |
| $\text{N–14}$ | $120.00$ | $101.33$ | $+46.67$ | $98.00$ | $116.67$ | $225$ / $232$ | $210$ / $213$ |
| $14\text{–}16$ | $96.00$ | $101.33$ | $+41.33$ | $116.67$ | $111.33$ | $220$ / $227$ | $200$ / $207$ |
| $\mathbf{16\text{–18 (Max } V\mathbf{)}}$ | $\mathbf{110.00}$ | $\mathbf{101.33}$ | $\mathbf{+50.00}$ | $\mathbf{111.33}$ | $\mathbf{120.00}$ | $\mathbf{210}$ / $\mathbf{218}$ | $\mathbf{205}$ / $\mathbf{206}$ |
| $18\text{–}20$ | $80.00$ | $101.33$ | $+28.67$ | $120.00$ | $98.67$ | $200$ / $211$ | $210$ / $208$ |
| $20\text{–}22$ | $90.00$ | $101.33$ | $+17.33$ | $98.67$ | $87.33$ | $180$ / $196$ | $185$ / $197$ |
| $22\text{–M}$ | $84.00$ | $101.33$ | $0.00$ | $87.33$ | $70.00$ | $160$ / $178$ | $175$ / $186$ |
| $\text{M–2}$ | $80.00$ | $101.33$ | $-21.33$ | $70.00$ | $48.67$ | $130$ / $153$ | $150$ / $167$ |
| $\mathbf{2\text{–4 (Min } C_{\text{eq}}\mathbf{)}}$ | $\mathbf{60.00}$ | $\mathbf{101.33}$ | $\mathbf{-62.67}$ | $\mathbf{48.67}$ | $\mathbf{7.33}$ | $\mathbf{110}$ / $\mathbf{129}$ | $\mathbf{135}$ / $\mathbf{149}$ |
| $\mathbf{4\text{–6 (Min } V\mathbf{)}}$ | $\mathbf{94.00}$ | $\mathbf{101.33}$ | $\mathbf{-70.00}$ | $\mathbf{7.33}$ | $\mathbf{0.00}$ | $\mathbf{160}$ / $\mathbf{158}$ | $\mathbf{150}$ / $\mathbf{150}$ |

**Bước 4 - Đánh giá biên độ dao động nồng độ $\text{BOD}$ và $\text{TSS}$ trước, sau điều hòa**: So sánh cực trị trước và sau bể điều hòa, dải dao động $\text{BOD}$ thu hẹp từ $110\text{–}245\text{ mg/L}$ về $129\text{–}240\text{ mg/L}$ và dải dao động $\text{TSS}$ thu hẹp từ $135\text{–}220\text{ mg/L}$ về $149\text{–}217\text{ mg/L}$ [Page 9].

$$
\left(\frac{\text{BOD}_{\max}}{\text{BOD}_{\min}}\right)_{\text{trước}} = \frac{245}{110} = 2.23 \implies \left(\frac{\text{BOD}_{\max}}{\text{BOD}_{\min}}\right)_{\text{sau}} = \frac{240}{129} = 1.86
$$

$$
\left(\frac{\text{TSS}_{\max}}{\text{TSS}_{\min}}\right)_{\text{trước}} = \frac{220}{135} = 1.63 \implies \left(\frac{\text{TSS}_{\max}}{\text{TSS}_{\min}}\right)_{\text{sau}} = \frac{217}{149} = 1.46
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Thể tích bể điều hòa lý thuyết ($V_{\text{theo}}$)**: $120\text{ m}^3$ (Kiểm tra: $50.00 - (-70.00) = 120.00\text{ m}^3\text{ — Đạt chuẩn Slide 9}$)
- **Thể tích bể điều hòa thực tế ($V_{\text{prac}}$)**: $144\text{ m}^3$ (Kiểm tra: $1.2 \times 120.00 = 144.00\text{ m}^3\text{ — Đạt chuẩn Slide 10}$)
- **Dải nồng độ $\text{BOD}$ sau điều hòa ($\text{BOD}_{\text{eq}}$)**: $129\text{–}240\text{ mg/L}$ (Kiểm tra: $\frac{\text{Peak}}{\text{Min}} = 1.86 < 2.23\text{ — Đạt chuẩn Slide 32}$)
- **Dải nồng độ $\text{TSS}$ sau điều hòa ($\text{TSS}_{\text{eq}}$)**: $149\text{–}217\text{ mg/L}$ (Kiểm tra: $\frac{\text{Peak}}{\text{Min}} = 1.46 < 1.63\text{ — Đạt chuẩn Slide 32}$)
