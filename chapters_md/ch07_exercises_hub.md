### Bài tập ch07_ex01 (Slide 6): Thiết kế bể thiếu khí đầu nguồn (Preanoxic) kết hợp bể lắng thứ cấp

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Thiết kế bể thiếu khí đầu nguồn (Preanoxic tank) dùng bể lắng thứ cấp với cùng thông số đầu vào và kết quả nitrat hóa của Bài tập `ch06_ex02` ($Q = 22,700\text{ m}^3/\text{ngày}$, $T = 12^\circ\text{C}$, $\text{BOD}_0 = 140\text{ g/m}^3$, $\text{bCOD}_0 = 224\text{ g/m}^3$, $\text{rbCOD}_0 = 80\text{ g/m}^3$, $\text{SRT} = 21\text{ ngày}$, $\text{NO}_x = 29.0\text{ g/m}^3$, thể tích bể hiếu khí $V_A = 13,418\text{ m}^3$, $X_{\text{TSS}} = 3,000\text{ g/m}^3$) để đạt nồng độ nitrat đầu ra $N_e = \text{NO}_3\text{-N} = 6.0\text{ g/m}^3$ [Page 2] [Page 3].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng và nhiệt độ nước thải | $Q, T$ | $22,700, 12$ | $\text{m}^3/\text{ngày}, ^\circ\text{C}$ (Slide 6) |
| Nồng độ $\text{BOD}_0$, $\text{bCOD}_0$ và $\text{rbCOD}_0$ | $\text{BOD}_0, S_0, \text{rbCOD}_0$ | $140, 224, 80$ | $\text{g/m}^3$ (Chương 6 Slide 16) |
| Nồng độ nitơ bị oxy hóa và $\text{NO}_3\text{-N}$ đầu ra | $\text{NO}_x, N_e$ | $29.0, 6.0$ | $\text{g/m}^3$ (Slide 5 và Slide 6) |
| Tỷ số tuần hoàn bùn hoạt tính từ bể lắng | $R$ | $0.60$ | $\text{không thứ nguyên}$ (Slide 5) |
| Tỷ lệ $\text{rbCOD}/\text{bCOD}$ và hệ số $\text{SDNR}$ | $b_0, b_1$ | $0.239, 0.147$ | $35.7\%\text{ rbCOD}$ (Chương 5.2 Slide 25) |
| Hệ số nhiệt độ của tốc độ khử nitrat riêng | $\theta_{\text{SDNR}}$ | $1.026$ | $\text{không thứ nguyên}$ (Chương 5.2 Slide 26) |
| Suất công suất khuấy trộn bể thiếu khí | $p_{\text{mix}}$ | $8.0$ | $\text{W/m}^3$ (Chương 5.2 Slide 22) |

**Bước 1 - Xác định tỷ số tuần hoàn nội bộ $\text{IR}$ và tải lượng nitrat nạp vào bể thiếu khí**: Áp dụng phương trình cân bằng nitrat trên Slide 5 với $\text{NO}_x = 29.0\text{ g/m}^3$, $N_e = 6.0\text{ g/m}^3$ và $R = 0.60$ cho tỷ số tuần hoàn nội bộ $\text{IR} = 3.23$ và tổng lượng nitrat nạp vào bể thiếu khí mỗi ngày là $\text{NO}_{x,\text{feed}} = 521.6\text{ kg/d}$ [Page 3].

$$\text{IR} = \frac{\text{NO}_x}{N_e} - 1 - R = \frac{29.0}{6.0} - 1 - 0.60 = 4.83 - 1.60 = 3.23$$

$$\text{NO}_{x,\text{feed}} = Q(\text{IR} + R) N_e = \frac{22,700 \times (3.23 + 0.60) \times 6.0}{10^3} = 521.6\text{ kg NO}_3\text{-N/d}$$

**Bước 2 - Tính nồng độ sinh khối dị dưỡng hoạt tính $X_b$ trong hệ thống**: Từ công thức sinh khối hoạt tính trên Slide 23 Chương 5.2 và số liệu Bài tập `ch06_ex02` ($\text{SRT} = 21\text{ ngày}$, $V_A = 13,418\text{ m}^3$), nồng độ sinh khối dị dưỡng hoạt tính đạt $X_b = 1,256\text{ g/m}^3$ [Page 3].

$$X_b = \frac{Q \cdot \text{SRT} \cdot Y_H (S_0 - S)}{V_A (1 + b_{H,12} \cdot \text{SRT})} = \frac{22,700 \times 21 \times 0.45 \times (224 - 0.3)}{13,418 \times (1 + 0.088 \times 21)} = 1,256\text{ g/m}^3$$

**Bước 3 - Xác định thể tích bể thiếu khí và kiểm tra khả năng khử nitrat $\text{NO}_r$**: Chọn thời gian lưu nước thiếu khí $\tau_{\text{nox}} = 2.2\text{ h}$ (sau khi thử $\tau_{\text{nox}} = 1.8\text{ h}$ chỉ đạt $\text{NO}_r = 476.7\text{ kg/d} < 521.6\text{ kg/d}$) cho thể tích bể thiếu khí $V_{\text{nox}} = 2,081\text{ m}^3$, tỷ số $F/M_b = 1.22\text{ g/g}\cdot\text{d}$, tốc độ khử nitrat hiệu chỉnh ở $12^\circ\text{C}$ đạt $\text{SDNR}_{12,\text{adj}} = 0.204\text{ g/g}\cdot\text{d}$ và khả năng khử nitrat đạt $\text{NO}_r = 532.3\text{ kg/d} \ge 521.6\text{ kg/d}$ (thỏa mãn) [Page 3].

$$V_{\text{nox}} = 22,700 \times \frac{2.2}{24} = 2,081\text{ m}^3, \quad F/M_b = \frac{Q \cdot \text{BOD}_0}{V_{\text{nox}} X_b} = \frac{22,700 \times 140}{2,081 \times 1,256} = 1.22\text{ g/g}\cdot\text{d}$$

$$\text{SDNR}_{20} = 0.239 + 0.147 \ln(1.22) = 0.268\text{ d}^{-1}, \quad \text{SDNR}_{20,\text{adj}} = 0.268 - 0.029 \ln(1.22) - 0.012 = 0.250\text{ d}^{-1}$$

$$\text{SDNR}_{12,\text{adj}} = 0.250 \times 1.026^{(12 - 20)} = 0.204\text{ d}^{-1} \implies \text{NO}_r = \frac{2,081 \times 1,256 \times 0.204}{10^3} = 532.3\text{ kg/d} \ge 521.6\text{ kg/d}$$

**Bước 4 - Tính lượng oxy tiết kiệm, độ kiềm phục hồi và công suất khuấy trộn**: Quá trình khử nitrat giúp tiết kiệm $\text{O}_{2,\text{credit}} = 1,493.2\text{ kg O}_2/\text{d}$ (giảm nhu cầu oxy thực xuống $R_{o,\text{net}} = 5,095.7\text{ kg O}_2/\text{d}$), phục hồi $\text{Alk}_{\text{rec}} = 82.1\text{ g/m}^3\text{ as CaCO}_3$ và cần công suất máy khuấy chìm $P_{\text{mix}} = 16.6\text{ kW}$ [Page 2] [Page 3].

$$\text{O}_{2,\text{credit}} = \frac{2.86 \times (29.0 - 6.0) \times 22,700}{10^3} = 1,493.2\text{ kg O}_2/\text{d} \implies R_{o,\text{net}} = 6,588.9 - 1,493.2 = 5,095.7\text{ kg O}_2/\text{d}$$

$$\text{Alk}_{\text{rec}} = 3.57 \times (29.0 - 6.0) = 82.1\text{ g/m}^3, \quad P_{\text{mix}} = \frac{8.0\text{ W/m}^3 \times 2,081\text{ m}^3}{10^3} = 16.6\text{ kW}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Tỷ số tuần hoàn nội bộ và tải lượng nitrat nạp ($\text{IR}, \text{NO}_{x,\text{feed}}$)**: $3.23$ và $521.6\text{ kg NO}_3\text{-N/d}$ (Kiểm tra: $\text{IR} = 3.23 \in [3, 4]\text{ — Đạt chuẩn Slide 5}$)
- **Nồng độ sinh khối dị dưỡng hoạt tính ($X_b$)**: $1,256\text{ g/m}^3$ (Kiểm tra: $X_b / X_{\text{TSS}} = 0.419\text{ — Đạt chuẩn Chương 5.2 Slide 23}$)
- **Thể tích bể thiếu khí và thời gian lưu nước ($V_{\text{nox}}, \tau_{\text{nox}}$)**: $2,081\text{ m}^3$ và $2.2\text{ h}$ (Kiểm tra: $\text{NO}_r = 532.3\text{ kg/d} \ge \text{NO}_{x,\text{feed}} = 521.6\text{ kg/d — Đạt chuẩn Slide 6}$)
- **Nhu cầu oxy thực tế và công suất máy khuấy ($R_{o,\text{net}}, P_{\text{mix}}$)**: $5,095.7\text{ kg O}_2/\text{d}$ và $16.6\text{ kW}$ (Kiểm tra: $p_{\text{mix}} = 8.0\text{ W/m}^3\text{ — Đạt chuẩn Chương 5.2 Slide 22}$)

### Bài tập ch07_ex02 (Slide 12): Thiết kế bể thiếu khí đầu nguồn kết hợp tách màng (Preanoxic MBR)

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Thiết kế bể thiếu khí đầu nguồn kết hợp tách màng (Preanoxic MBR) với cùng thông số đầu vào và kết quả của Bài tập `ch06_ex03` ($Q = 22,700\text{ m}^3/\text{ngày}$, $T = 12^\circ\text{C}$, $\text{SRT} = 21\text{ ngày}$, $\text{NO}_x = 29.0\text{ g/m}^3$, tỷ số tuần hoàn bùn từ bể màng về đầu bể thiếu khí $R = 6$, nồng độ bùn bể màng $X_m = 12,000\text{ g/m}^3$, nồng độ bùn vùng phản ứng $X_A = 10,286\text{ g/m}^3$) và không sử dụng tuần hoàn nội bộ ($\text{IR} = 0$) [Page 4].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng thiết kế và nhiệt độ vận hành | $Q, T$ | $22,700, 12$ | $\text{m}^3/\text{ngày}, ^\circ\text{C}$ (Slide 12) |
| Tỷ số tuần hoàn nội bộ và tuần hoàn bùn màng | $\text{IR}, R$ | $0, 6.0$ | $\text{không thứ nguyên}$ (Slide 12) |
| Nồng độ $\text{MLSS}$ trong bể màng và vùng phản ứng | $X_m, X_A$ | $12,000, 10,286$ | $\text{g/m}^3$ (Chương 6 Slide 43) |
| Tổng khối lượng sinh khối hoạt tính và $\text{MLSS}$ | $\text{Mass}_{X_b}, \text{Mass}_{\text{MLSS}}$ | $16,849, 40,253$ | $\text{kg}$ (Chương 6 Slide 43) |
| Tỷ lệ sinh khối dị dưỡng hoạt tính trong $\text{MLSS}$ | $f_{\text{active}}$ | $0.4186$ | $\text{không thứ nguyên}$ (Slide 12) |
| Hệ số phương trình $\text{SDNR}$ ở $35.7\%\text{ rbCOD}$ | $b_0, b_1, \theta_{\text{SDNR}}$ | $0.239, 0.147, 1.026$ | $\text{Chương 5.2 Slide 25–26}$ |

**Bước 1 - Tính nồng độ nitrat đầu ra $N_e$ và tải lượng nitrat nạp vào bể thiếu khí**: Trong sơ đồ MBR trên Slide 12 với $\text{IR} = 0$ và dòng bùn tuần hoàn $R = 6$ quay về đầu bể thiếu khí, nồng độ nitrat đầu ra đạt $N_e = 4.14\text{ g/m}^3 \le 6.0\text{ g/m}^3$ và tải lượng nitrat nạp vào bể thiếu khí là $\text{NO}_{x,\text{feed}} = 564.3\text{ kg/d}$ [Page 3] [Page 4].

$$\text{NO}_x = (1 + \text{IR} + R) N_e = (1 + 0 + 6) N_e = 7 N_e \implies N_e = \frac{29.0}{7} = 4.14\text{ g/m}^3 \le 6.0\text{ g/m}^3$$

$$\text{NO}_{x,\text{feed}} = Q \cdot R \cdot N_e = \frac{22,700 \times 6 \times 4.14}{10^3} = 564.3\text{ kg NO}_3\text{-N/d}$$

**Bước 2 - Tính nồng độ sinh khối dị dưỡng hoạt tính $X_{b,\text{MBR}}$ trong bể thiếu khí**: Nhân tỷ lệ sinh khối hoạt tính $f_{\text{active}} = 0.4186$ với nồng độ bùn $X_A = 10,286\text{ g/m}^3$ cho nồng độ sinh khối dị dưỡng hoạt tính trong bể thiếu khí của cụm MBR là $X_{b,\text{MBR}} = 4,305\text{ g/m}^3$ [Page 4].

$$f_{\text{active}} = \frac{\text{Mass}_{X_b}}{\text{Mass}_{\text{MLSS}}} = \frac{16,849}{40,253} = 0.4186 \implies X_{b,\text{MBR}} = 0.4186 \times 10,286 = 4,305\text{ g/m}^3$$

**Bước 3 - Xác định thể tích bể thiếu khí $V_{\text{nox}}$ và công suất khuấy trộn của cụm MBR**: Chọn thể tích bể thiếu khí $V_{\text{nox}} = 700\text{ m}^3$ ($\tau_{\text{nox}} = 0.74\text{ h}$, sau khi thử $V_{\text{nox}} = 550\text{ m}^3$ chỉ đạt $\text{NO}_r = 504.7\text{ kg/d} < 564.3\text{ kg/d}$) cho $F/M_b = 1.05\text{ g/g}\cdot\text{d}$, $\text{SDNR}_{12,\text{adj}} = 0.190\text{ g/g}\cdot\text{d}$, khả năng khử nitrat đạt $\text{NO}_r = 572.5\text{ kg/d} \ge 564.3\text{ kg/d}$ (thỏa mãn) và công suất khuấy trộn đạt $P_{\text{mix}} = 5.6\text{ kW}$ [Page 4].

$$F/M_b = \frac{22,700 \times 140}{700 \times 4,305} = 1.05\text{ g/g}\cdot\text{d}, \quad \text{SDNR}_{20} = 0.239 + 0.147 \ln(1.05) = 0.246\text{ d}^{-1}$$

$$\text{SDNR}_{20,\text{adj}} = 0.246 - 0.029 \ln(1.05) - 0.012 = 0.233\text{ d}^{-1}, \quad \text{SDNR}_{12,\text{adj}} = 0.233 \times 1.026^{-8} = 0.190\text{ d}^{-1}$$

$$\text{NO}_r = \frac{700 \times 4,305 \times 0.190}{10^3} = 572.5\text{ kg/d} \ge 564.3\text{ kg/d}, \quad P_{\text{mix}} = \frac{8.0 \times 700}{10^3} = 5.6\text{ kW}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Nồng độ nitrat đầu ra và tải lượng nitrat nạp ($N_e, \text{NO}_{x,\text{feed}}$)**: $4.14\text{ g/m}^3$ và $564.3\text{ kg NO}_3\text{-N/d}$ (Kiểm tra: $N_e = 4.14\text{ g/m}^3 \le 6.0\text{ g/m}^3\text{ với IR} = 0\text{ — Đạt chuẩn Slide 12}$)
- **Nồng độ sinh khối hoạt tính trong bể thiếu khí MBR ($X_{b,\text{MBR}}$)**: $4,305\text{ g/m}^3$ (Kiểm tra: $X_A = 10,286\text{ g/m}^3\text{ tại }R = 6\text{ — Đạt chuẩn Chương 6 Slide 39}$)
- **Thể tích bể thiếu khí và khả năng khử nitrat ($V_{\text{nox}}, \text{NO}_r$)**: $700\text{ m}^3$ ($\tau_{\text{nox}} = 0.74\text{ h}$) và $572.5\text{ kg/d}$ (Kiểm tra: $\text{NO}_r = 572.5\text{ kg/d} \ge 564.3\text{ kg/d — Đạt chuẩn Slide 12}$)
- **Công suất khuấy trộn bể thiếu khí ($P_{\text{mix}}$)**: $5.6\text{ kW}$ (Kiểm tra: $p_{\text{mix}} = 8.0\text{ W/m}^3\text{ — Đạt chuẩn Chương 5.2 Slide 22}$)

### Bài tập ch07_ex03 (Slide 20): Thiết kế và kiểm tra quá trình khử nitrat trong bể SBR

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Thiết kế và kiểm tra khả năng khử nitrat trong giai đoạn làm đầy khuấy trộn thiếu khí ($t_{\text{anoxic}} = 2.0\text{ h}$) của hệ thống $N = 2\text{ bể SBR}$ lấy cùng thông số đầu vào và kết quả của Bài tập `ch06_ex04` ($Q = 7,570\text{ m}^3/\text{ngày}$, $T = 12^\circ\text{C}$, chu kỳ $t_c = 6.0\text{ h}$ gồm $8\text{ mẻ/ngày}$ cho $2\text{ bể}$, thể tích làm đầy $V_F = 946.25\text{ m}^3/\text{mẻ}$, thể tích đầy bể $V_T = 4,731.25\text{ m}^3/\text{bể}$, thể tích giữ lại sau chắt nước $V_S = 3,785\text{ m}^3/\text{bể}$, $\text{SRT} = 26.5\text{ ngày}$, $\text{NO}_x = 26.2\text{ g/m}^3$, $\text{BOD}_0 = 220\text{ g/m}^3$, $\text{bCOD}_0 = 352\text{ g/m}^3$) [Page 4] [Page 5].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng thiết kế và tổng số mẻ mỗi ngày | $Q, n_{\text{cycles}}$ | $7,570, 8$ | $\text{m}^3/\text{ngày}, \text{mẻ/ngày}$ (Slide 20) |
| Thể tích làm đầy, thể tích đầy và thể tích giữ lại | $V_F, V_T, V_S$ | $946.25, 4,731.25, 3,785$ | $\text{m}^3/\text{bể}$ (Chương 6 Slide 51) |
| Thời gian làm đầy tổng và làm đầy thiếu khí | $t_F, t_{\text{anoxic}}$ | $3.0, 2.0$ | $\text{giờ/mẻ}$ (Slide 19 và Slide 20) |
| Thời gian lưu bùn và nồng độ nitơ oxy hóa | $\text{SRT}, \text{NO}_x$ | $26.5, 26.2$ | $\text{ngày}, \text{g/m}^3$ (Chương 6 Slide 51) |
| Nồng độ $\text{BOD}_0$ và $\text{bCOD}_0$ đầu vào | $\text{BOD}_0, S_0$ | $220, 352$ | $\text{g/m}^3$ (Chương 6 Slide 51) |
| Hệ số $\text{SDNR}$ tuyến tính khi $F/M_b \le 0.5$ | $k_{\text{SDNR}}, \theta_{\text{SDNR}}$ | $0.24, 1.026$ | $\text{Chương 5.2 Slide 25–26}$ |

**Bước 1 - Tính lượng nitrat sinh ra mỗi mẻ, nồng độ nitrat đầu ra và lượng nitrat tồn dư sau chắt nước**: Lượng nitrat tạo thành trong mỗi mẻ là $\text{NO}_{x,\text{cycle}} = 24,792\text{ g/mẻ}$; khi toàn bộ nitrat trong thể tích đệm $V_S = 3,785\text{ m}^3$ được khử hết ở kỳ làm đầy thiếu khí, nồng độ nitrat đầu ra ở cuối mẻ đạt $N_{e,\text{NO}_3} = 5.24\text{ g/m}^3$ và lượng nitrat giữ lại trong $V_S$ cần khử ở mẻ tiếp theo là $\text{NO}_3\text{-N}_{\text{rem}} = 19,833\text{ g/mẻ}$ [Page 4] [Page 5].

$$\text{NO}_{x,\text{cycle}} = V_F \times \text{NO}_x = 946.25 \times 26.2 = 24,792\text{ g NO}_3\text{-N/mẻ}$$

$$N_{e,\text{NO}_3} = \frac{24,792\text{ g}}{4,731.25\text{ m}^3} = 5.24\text{ g/m}^3, \quad \text{NO}_3\text{-N}_{\text{rem}} = 3,785 \times 5.24 = 19,833\text{ g NO}_3\text{-N/mẻ}$$

**Bước 2 - Tính khối lượng sinh khối dị dưỡng hoạt tính và tỷ số $F/M_b$ trong kỳ làm đầy**: Khối lượng sinh khối dị dưỡng hoạt tính trong mỗi bể SBR tại $\text{SRT} = 26.5\text{ ngày}$ đạt $\text{Mass}_{X_b,1\text{tank}} = 4,764.2\text{ kg}$ và lưu lượng nạp vào $1\text{ bể}$ trong $3.0\text{ h}$ làm đầy là $Q_{\text{fill}} = 7,570\text{ m}^3/\text{d}$, cho tỷ số $F/M_b = 0.35\text{ g BOD/g biomass}\cdot\text{d}$ [Page 5].

$$\text{Mass}_{X_b,1\text{tank}} = \frac{1}{2} \times \frac{7,570 \times 26.5 \times 0.45 \times (352 - 0.3)}{(1 + 0.088 \times 26.5)\times 10^3} = 4,764.2\text{ kg/bể}$$

$$Q_{\text{fill}} = \frac{946.25\text{ m}^3}{3.0\text{ h}} \times 24\text{ h/d} = 7,570\text{ m}^3/\text{d} \implies F/M_b = \frac{7,570 \times 220 \times 10^{-3}}{4,764.2} = 0.35\text{ g/g}\cdot\text{d}$$

**Bước 3 - Tính tốc độ khử nitrat riêng $\text{SDNR}_{12}$ và kiểm tra khả năng khử nitrat trong $2.0\text{ h}$ làm đầy thiếu khí**: Vì $F/M_b = 0.35 \le 0.5$, áp dụng phương trình tuyến tính trên Slide 25 Chương 5.2 cho $\text{SDNR}_{20} = 0.084\text{ g/g}\cdot\text{d}$ và $\text{SDNR}_{12} = 0.068\text{ g/g}\cdot\text{d}$, suy ra khả năng khử nitrat trong $2.0\text{ h}$ làm đầy thiếu khí đạt $\text{NO}_{r,\text{cycle}} = 27,125\text{ g/mẻ} \ge 19,833\text{ g/mẻ}$ (thỏa mãn) và giảm nhu cầu oxy thực xuống $R_{o,\text{net}} = 2,415.8\text{ kg O}_2/\text{d}$ [Page 5].

$$\text{SDNR}_{20} = 0.24 \times (F/M_b) = 0.24 \times 0.35 = 0.084\text{ d}^{-1}, \quad \text{SDNR}_{12} = 0.084 \times 1.026^{(12 - 20)} = 0.068\text{ d}^{-1}$$

$$\text{NO}_{r,\text{cycle}} = 4,764.2 \times 10^3 \times 0.068 \times \frac{2.0\text{ h}}{24\text{ h/d}} = 27,125\text{ g/mẻ} \ge 19,833\text{ g/mẻ}$$

$$\text{O}_{2,\text{credit}} = \frac{2.86 \times 8 \times 19,833}{10^3} = 453.9\text{ kg O}_2/\text{d} \implies R_{o,\text{net}} = 2,869.7 - 453.9 = 2,415.8\text{ kg O}_2/\text{d}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Nồng độ nitrat đầu ra và lượng nitrat tồn dư mỗi mẻ ($N_{e,\text{NO}_3}, \text{NO}_3\text{-N}_{\text{rem}}$)**: $5.24\text{ g/m}^3$ và $19,833\text{ g/mẻ}$ (Kiểm tra: $N_{e,\text{NO}_3} = 5.24\text{ g/m}^3 \le 6.0\text{ g/m}^3\text{ — Đạt chuẩn Slide 19 và Slide 20}$)
- **Khối lượng sinh khối hoạt tính mỗi bể và tỷ số $F/M_b$ ($\text{Mass}_{X_b,1\text{tank}}, F/M_b$)**: $4,764.2\text{ kg}$ và $0.35\text{ g BOD/g biomass}\cdot\text{d}$ (Kiểm tra: $F/M_b = 0.35 \le 0.5\text{ — Đạt chuẩn Chương 5.2 Slide 25}$)
- **Tốc độ khử nitrat riêng và khả năng khử mỗi mẻ ($\text{SDNR}_{12}, \text{NO}_{r,\text{cycle}}$)**: $0.068\text{ g/g}\cdot\text{d}$ và $27,125\text{ g/mẻ}$ (Kiểm tra: $\text{NO}_{r,\text{cycle}} = 27,125\text{ g/mẻ} \ge 19,833\text{ g/mẻ — Đạt chuẩn Slide 20}$)
- **Nhu cầu oxy thực tế sau khi trừ tín dụng khử nitrat ($R_{o,\text{net}}$)**: $2,415.8\text{ kg O}_2/\text{d}$ (Kiểm tra: Tiết kiệm $453.9\text{ kg O}_2/\text{d}$ và phục hồi $74.8\text{ g/m}^3\text{ CaCO}_3\text{ — Đạt chuẩn Slide 20}$)
