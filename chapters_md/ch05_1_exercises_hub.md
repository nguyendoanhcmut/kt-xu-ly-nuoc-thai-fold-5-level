### Bài tập ch05_1_ex01 (Slide 22–23, Trang 11–12): Tính Hệ số Sản lượng Quan sát và Lượng Oxy Tiêu thụ của Bể Hiếu khí

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Một bể phản ứng sinh học hiếu khí tiếp nhận nước thải có lưu lượng $Q = 1000\text{ m}^3/\text{d}$ với nồng độ chất hữu cơ hòa tan dễ phân hủy sinh học đầu vào $S_0 = 500\text{ g/m}^3$ và không có sinh khối đầu vào ($X_0 = 0\text{ g/m}^3$) [Page 11] [Page 12]. Dòng nước ra khỏi bể phản ứng có nồng độ cơ chất $S = 10\text{ g/m}^3$ và nồng độ chất rắn lơ lửng bay hơi $X_e = 200\text{ g VSS/m}^3$. Hãy xác định hệ số sản lượng sinh khối quan sát được $Y_{\text{obs}}$ ($\text{g VSS/g COD}$) và lượng oxy tiêu thụ theo tỷ lệ $\text{g O}_2/\text{g COD}$ cùng tổng khối lượng oxy tiêu thụ mỗi ngày $R_{O_2}$ ($\text{g/d}$ và $\text{kg/d}$).

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng nước thải đầu vào | $Q$ | $1000$ | $\text{m}^3/\text{d}$ (Slide $22$) |
| Nồng độ $\text{bsCOD}$ đầu vào | $S_0$ | $500$ | $\text{g/m}^3$ (Slide $22$) |
| Nồng độ $\text{bsCOD}$ đầu ra | $S$ | $10$ | $\text{g/m}^3$ (Slide $22$) |
| Nồng độ sinh khối đầu vào | $X_0$ | $0$ | $\text{g VSS/m}^3$ (Slide $23$) |
| Nồng độ sinh khối $\text{VSS}$ đầu ra | $X_e$ | $200$ | $\text{g VSS/m}^3$ (Slide $22$) |
| Đương lượng $\text{COD}$ của tế bào $\text{C}_5\text{H}_7\text{NO}_2$ | $f_{\text{COD}}$ | $1.42$ | $\text{g O}_2/\text{g VSS}$ (Slide $20$) |

**Bước 1 - Tính nồng độ cơ chất bị khử và hệ số sản lượng quan sát**: Hiệu số giữa nồng độ cơ chất đầu vào $S_0$ và đầu ra $S$ cho độ giảm cơ chất $\Delta S = 490\text{ g COD/m}^3$ [Page 8]. Tỷ số giữa sinh khối tạo thành $\Delta X = 200\text{ g VSS/m}^3$ và độ giảm cơ chất $\Delta S$ xác định hệ số sản lượng quan sát $Y_{\text{obs}} = 0.41\text{ g VSS/g COD}$.

$$\Delta S = S_0 - S = 500 - 10 = 490\text{ (g COD/m}^3\text{)}$$

$$Y_{\text{obs}} = \frac{X_e - X_0}{S_0 - S} = \frac{200 - 0}{500 - 10} = \frac{200}{490} = 0.408 \approx 0.41\text{ (g VSS/g COD)}$$

**Bước 2 - Tính lượng oxy tiêu thụ trên mỗi gam cơ chất bị khử**: Mỗi gam sinh khối tế bào $\text{C}_5\text{H}_7\text{NO}_2$ tích lũy một lượng đương lượng oxy bằng $1.42\text{ g O}_2/\text{g VSS}$ [Page 10]. Phần cơ chất chuyển vào tế bào bằng $0.58\text{ g COD/g COD}$, do đó phần cơ chất bị oxy hóa bởi oxy hòa tan bằng $0.42\text{ g O}_2/\text{g COD}$.

$$\text{COD}_{\text{cell}} = 1.42 \times Y_{\text{obs}} = 1.42 \times \frac{200}{490} = 0.58\text{ (g COD/g COD)}$$

$$\frac{\text{O}_2}{\text{COD}_{\text{removed}}} = 1.00 - \text{COD}_{\text{cell}} = 1.00 - 0.58 = 0.42\text{ (g O}_2/\text{g COD)}$$

**Bước 3 - Tính tổng khối lượng oxy tiêu thụ mỗi ngày**: Cân bằng khối lượng $\text{COD}$ toàn bể lấy tổng tải lượng $\text{bsCOD}$ khử mỗi ngày trừ đi tải lượng $\text{COD}$ tích lũy trong bùn sinh học [Page 10]. Kết quả thu được tổng lượng oxy tiêu thụ mỗi ngày đạt $R_{O_2} = 206,000\text{ g O}_2/\text{d}$ hay $206\text{ kg O}_2/\text{d}$.

$$M_{\text{COD,removed}} = Q \times (S_0 - S) = 1000 \times (500 - 10) = 490,000\text{ (g COD/d)}$$

$$R_{O_2} = Q(S_0 - S) - 1.42 Q X_e = 490,000 - 1.42 \times 1000 \times 200 = 206,000\text{ (g O}_2/\text{d)}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Hệ số sản lượng sinh khối quan sát ($Y_{\text{obs}}$)**: $0.41\text{ g VSS/g COD}$ (Kiểm tra: $Y_{\text{obs}} = 0.408\text{ g/g} < Y_{\text{typical}} = 0.45\text{ g/g}\text{ — Đạt chuẩn Slide 18}$)
- **Tỷ lệ oxy tiêu thụ đơn vị ($\text{O}_2/\Delta\text{COD}$)**: $0.42\text{ g O}_2/\text{g COD}$ (Kiểm tra: $0.42 + 0.58 = 1.00\text{ g COD/g COD}\text{ — Đạt chuẩn cân bằng Slide 20}$)
- **Khối lượng oxy tiêu thụ hàng ngày ($R_{O_2}$)**: $206,000\text{ g O}_2/\text{d} = 206\text{ kg O}_2/\text{d}$ (Kiểm tra: $490 - 284 = 206\text{ kg O}_2/\text{d}\text{ — Đạt chuẩn Slide 19–20}$)

### Bài tập ch05_1_ex02 (Slide 36, Trang 17): Tính Sản lượng Sinh khối Ròng, Sản lượng Quan sát và Tỷ phần Hoạt tính trong Bể Khuấy trộn Hoàn toàn

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Một bể phản ứng hiếu khí khuấy trộn hoàn toàn có thể tích $V = 335\text{ m}^3$ và duy trì nồng độ sinh khối hoạt tính $X = 2000\text{ g/m}^3$ [Page 15] [Page 16] [Page 17]. Bể xử lý lưu lượng nước thải $Q = 1000\text{ m}^3/\text{d}$ có nồng độ cơ chất dễ phân hủy đầu vào $S_0 = 300\text{ g/m}^3$, nồng độ chất rắn bay hơi không phân hủy sinh học đầu vào $X_{o,i} = 50\text{ g/m}^3$, nồng độ cơ chất đầu ra $S = 2.4\text{ g/m}^3$ và hệ số xác tế bào $f_d = 0.1$. Sử dụng bảng hệ số động học chuẩn ở $20^\circ\text{C}$ trên Slide $31$, hãy xác định hệ số sản lượng sinh khối ròng $Y_{\text{bio}}$, hệ số sản lượng quan sát $Y_{\text{obs}}$ và tỷ phần sinh khối hoạt tính trong bùn hoạt tính $F_{X,\text{act}}$.

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Thể tích bể phản ứng hiếu khí | $V$ | $335$ | $\text{m}^3$ (Slide $36$) |
| Nồng độ sinh khối hoạt tính trong bể | $X$ | $2000$ | $\text{g VSS/m}^3$ (Slide $36$) |
| Lưu lượng nước thải đầu vào | $Q$ | $1000$ | $\text{m}^3/\text{d}$ (Slide $36$) |
| Nồng độ $\text{bsCOD}$ đầu vào | $S_0$ | $300$ | $\text{g/m}^3$ (Slide $36$) |
| Nồng độ $\text{bsCOD}$ đầu ra | $S$ | $2.4$ | $\text{g/m}^3$ (Slide $36$) |
| Nồng độ $\text{nbVSS}$ đầu vào | $X_{o,i}$ | $50$ | $\text{g/m}^3$ (Slide $36$) |
| Hệ số xác tế bào còn lại sau phân hủy | $f_d$ | $0.1$ | $\text{g VSS/g VSS}$ (Slide $36$) |
| Hệ số sản lượng tổng hợp chuẩn ở $20^\circ\text{C}$ | $Y$ | $0.45$ | $\text{g VSS/g COD}$ (Slide $31$) |
| Hệ số phân hủy nội bào chuẩn ở $20^\circ\text{C}$ | $b$ | $0.10$ | $\text{g VSS/g VSS}\cdot\text{d}$ (Slide $31$) |

**Bước 1 - Tính tốc độ sử dụng cơ chất theo đơn vị thể tích bể**: Từ phương trình cân bằng cơ chất ở trạng thái ổn định, tốc độ sử dụng cơ chất $r_{su}$ bằng tải lượng $\text{bsCOD}$ khử mỗi ngày chia cho thể tích bể $V$ [Page 13] [Page 15]. Kết quả thu được tốc độ tiêu thụ cơ chất đạt $r_{su} = 888.4\text{ g bsCOD/m}^3\cdot\text{d}$.

$$r_{su} = \frac{Q(S_0 - S)}{V} = \frac{1000 \times (300 - 2.4)}{335} = 888.4\text{ (g bsCOD/m}^3\cdot\text{d)}$$

**Bước 2 - Tính tốc độ tăng trưởng sinh khối hoạt tính ròng và tổng tốc độ sinh bùn**: Tốc độ tăng trưởng sinh khối ròng $r_X$ bằng tốc độ tổng hợp mới trừ đi tốc độ phân hủy nội bào đạt $199.8\text{ g VSS/m}^3\cdot\text{d}$ [Page 14] [Page 16]. Khi cộng thêm phần xác tế bào nội bào và lượng $\text{nbVSS}$ từ nước thải đầu vào, tổng tốc độ sinh bùn bay hơi đạt $r_{X_T,\text{VSS}} = 369.1\text{ g VSS/m}^3\cdot\text{d}$.

$$r_X = Y r_{su} - b X = 0.45 \times 888.4 - 0.10 \times 2000 = 199.8\text{ (g VSS/m}^3\cdot\text{d)}$$

$$r_{X_T,\text{VSS}} = r_X + f_d b X + \frac{Q X_{o,i}}{V} = 199.8 + 0.1 \times 0.10 \times 2000 + \frac{1000 \times 50}{335} = 369.1\text{ (g/m}^3\cdot\text{d)}$$

**Bước 3 - Tính hệ số sản lượng ròng, sản lượng quan sát và tỷ phần sinh khối hoạt tính**: Chia tốc độ sinh trưởng ròng $r_X$ và tổng tốc độ sinh bùn $r_{X_T,\text{VSS}}$ cho $r_{su}$ xác định được $Y_{\text{bio}} = 0.225\text{ g VSS/g bsCOD}$ và $Y_{\text{obs}} = 0.415\text{ g VSS/g bsCOD}$ [Page 16] [Page 17]. Tỷ số giữa $r_X$ và $r_{X_T,\text{VSS}}$ cho tỷ phần sinh khối hoạt tính trong $\text{MLVSS}$ đạt $F_{X,\text{act}} = 0.541$ hay $54.1\%$.

$$Y_{\text{bio}} = \frac{r_X}{r_{su}} = \frac{199.8}{888.4} = 0.225\text{ (g VSS/g bsCOD)}$$

$$Y_{\text{obs}} = \frac{r_{X_T,\text{VSS}}}{r_{su}} = \frac{369.1}{888.4} = 0.415\text{ (g VSS/g bsCOD)}$$

$$F_{X,\text{act}} = \frac{Y r_{su} - b X}{r_{X_T,\text{VSS}}} = \frac{199.8}{369.1} = 0.541 = 54.1\%$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Tốc độ sử dụng cơ chất ($r_{su}$)**: $888.4\text{ g bsCOD/m}^3\cdot\text{d}$ (Kiểm tra: $r_{su} \approx \frac{6 \times 2.4 \times 2000}{30 + 2.4} = 888.9\text{ g/m}^3\cdot\text{d}\text{ — Đạt chuẩn Slide 28, 31}$)
- **Hệ số sản lượng sinh khối ròng ($Y_{\text{bio}}$)**: $0.225\text{ g VSS/g bsCOD}$ (Kiểm tra: $Y_{\text{bio}} = 0.225\text{ g/g} < Y = 0.45\text{ g/g}\text{ — Đạt chuẩn Slide 35}$)
- **Hệ số sản lượng quan sát ($Y_{\text{obs}}$)**: $0.415\text{ g VSS/g bsCOD}$ (Kiểm tra: $Y_{\text{bio}} < Y_{\text{obs}} = 0.415\text{ g/g} < Y = 0.45\text{ g/g}\text{ — Đạt chuẩn Slide 35}$)
- **Tỷ phần sinh khối hoạt tính trong $\text{MLVSS}$ ($F_{X,\text{act}}$)**: $0.541 = 54.1\%$ (Kiểm tra: $\frac{Y_{\text{bio}}}{Y_{\text{obs}}} = \frac{0.225}{0.415} = 0.542\text{ — Đạt chuẩn Slide 34}$)

### Bài tập ch05_1_ex03 (Slide 52–53, Trang 24–25): Thiết kế Toàn diện Bể Bùn Hoạt tính Khuấy trộn Hoàn toàn

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Một hệ thống bùn hoạt tính sinh trưởng lơ lửng khuấy trộn hoàn toàn vận hành với thời gian lưu bùn $\text{SRT} = 6\text{ d}$ và lưu lượng nước thải $Q = 1000\text{ m}^3/\text{d}$ [Page 24] [Page 25]. Nước thải đầu vào có nồng độ cơ chất dễ phân hủy $S_0 = 192\text{ g/m}^3$, chất rắn trơ đầu vào bằng $10\text{ g/m}^3$, nồng độ $\text{nbVSS}$ đầu vào $X_{o,i} = 30\text{ g/m}^3$ và nồng độ bùn hoạt tính bay hơi duy trì trong bể hiếu khí $X_T = 2500\text{ g/m}^3$. Cho bộ hệ số động học gồm $k = 12.5\text{ g COD/g VSS}\cdot\text{d}$, $K_s = 10\text{ g COD/m}^3$, $Y = 0.4\text{ g VSS/g COD}$, $f_d = 0.15\text{ g VSS/g VSS}$, $b = 0.1\text{ g VSS/g VSS}\cdot\text{d}$ và tỷ số $\text{VSS}/\text{TSS} = 0.85$. Hãy xác định: (1) nồng độ $\text{bsCOD}$ đầu ra $S$, (2) thời gian lưu nước $\text{HRT}$, (3) lượng bùn sinh ra mỗi ngày $P_{X,\text{VSS}}$ và $P_{X,\text{TSS}}$, (4) tỷ phần sinh khối trong $\text{MLVSS}$, và (5) nhu cầu oxy hàng ngày $R_o$.

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Thời gian lưu bùn thiết kế | $\text{SRT}$ | $6$ | $\text{d}$ (Slide $52$) |
| Lưu lượng nước thải đầu vào | $Q$ | $1000$ | $\text{m}^3/\text{d}$ (Slide $52$) |
| Nồng độ $\text{bsCOD}$ đầu vào | $S_0$ | $192$ | $\text{g/m}^3$ (Slide $52$) |
| Nồng độ chất trơ đầu vào | $\text{TSS}_0 - \text{VSS}_0$ | $10$ | $\text{g/m}^3$ (Slide $52$) |
| Nồng độ $\text{MLVSS}$ trong bể hiếu khí | $X_T$ | $2500$ | $\text{g/m}^3$ (Slide $52$) |
| Nồng độ $\text{nbVSS}$ đầu vào | $X_{o,i}$ | $30$ | $\text{g/m}^3$ (Slide $52$) |
| Tốc độ sử dụng cơ chất riêng cực đại | $k$ | $12.5$ | $\text{g COD/g VSS}\cdot\text{d}$ (Slide $52$) |
| Hằng số bán bão hòa tốc độ | $K_s$ | $10$ | $\text{g COD/m}^3$ (Slide $52$) |
| Hệ số sản lượng tổng hợp sinh khối | $Y$ | $0.4$ | $\text{g VSS/g COD}$ (Slide $52$) |
| Tỷ phần xác tế bào không phân hủy | $f_d$ | $0.15$ | $\text{g VSS/g VSS}$ (Slide $52$) |
| Hệ số phân hủy nội bào | $b$ | $0.1$ | $\text{g VSS/g VSS}\cdot\text{d}$ (Slide $52$) |
| Tỷ lệ chất rắn bay hơi của sinh khối | $\text{VSS}/\text{TSS}$ | $0.85$ | $\text{g VSS/g TSS}$ (Slide $52$) |

**Bước 1 - Tính nồng độ cơ chất hòa tan dễ phân hủy ở dòng ra**: Thay thời gian lưu bùn $\text{SRT} = 6\text{ d}$ và các hệ số động học vào phương trình cân bằng cơ chất trên Slide $45$ [Page 21]. Nồng độ cơ chất dễ phân hủy sinh học còn lại ở dòng ra đạt $S = 0.56\text{ g/m}^3$.

$$S = \frac{K_s (1 + b \times \text{SRT})}{\text{SRT}(Y k - b) - 1} = \frac{10 \times (1 + 0.1 \times 6)}{6 \times (0.4 \times 12.5 - 0.1) - 1} = \frac{16}{28.4} = 0.56\text{ (g/m}^3\text{)}$$

**Bước 2 - Tính lượng bùn hoạt tính sinh ra mỗi ngày theo chất rắn bay hơi**: Tổng lượng bùn bay hơi sinh ra mỗi ngày $P_{X,\text{VSS}}$ bằng tổng của sinh khối dị dưỡng hoạt tính $A$, xác tế bào nội bào $B$ và lượng $\text{nbVSS}$ đầu vào $C$ theo phương trình trên Slide $48$ [Page 22]. Kết quả thu được $P_{X,\text{VSS}} = 82.17\text{ kg VSS/d}$, trong đó tổng sinh khối sinh học chiếm $P_{X,\text{bio}} = A + B = 52.17\text{ kg VSS/d}$.

$$A = \frac{Q Y (S_0 - S)}{1 + b \times \text{SRT}} = \frac{1000 \times 0.4 \times (192 - 0.56)}{1 + 0.1 \times 6} = 47.86\text{ (kg VSS/d)}$$

$$B = f_d b \times \text{SRT} \times A = 0.15 \times 0.1 \times 6 \times 47.86 = 4.31\text{ (kg VSS/d)}$$

$$P_{X,\text{VSS}} = A + B + Q X_{o,i} = 47.86 + 4.31 + 30.00 = 82.17\text{ (kg VSS/d)}$$

**Bước 3 - Tính lượng bùn sinh ra mỗi ngày theo tổng chất rắn lơ lửng**: Chia phần sinh khối sinh học $(A + B)$ cho tỷ số $0.85$ và cộng thêm lượng $\text{nbVSS}$ cùng chất rắn vô cơ đầu vào theo phương trình trên Slide $49$ [Page 23]. Tổng lượng bùn khô sinh ra mỗi ngày đạt $P_{X,\text{TSS}} = 101.37\text{ kg TSS/d}$ (hoặc bằng $91.37\text{ kg TSS/d}$ nếu thông số $10\text{ g/m}^3$ là chất hữu cơ hòa tan trơ).

$$P_{X,\text{TSS}} = \frac{A + B}{0.85} + C + Q(\text{TSS}_0 - \text{VSS}_0) = \frac{47.86 + 4.31}{0.85} + 30.00 + 10.00 = 101.37\text{ (kg TSS/d)}$$

**Bước 4 - Tính thể tích bể hiếu khí và thời gian lưu nước**: Từ quan hệ bảo toàn khối lượng bùn $V \times X_T = P_{X,\text{VSS}} \times \text{SRT}$ trên Slide $46$, thể tích bể hiếu khí bằng $V = 197.2\text{ m}^3$ [Page 21]. Chia thể tích bể $V$ cho lưu lượng $Q$ xác định được thời gian lưu nước $\text{HRT} = 0.197\text{ d}$ hay $4.73\text{ h}$.

$$V = \frac{P_{X,\text{VSS}} \times \text{SRT}}{X_T} = \frac{82,166 \times 6}{2500} = 197.2\text{ (m}^3\text{)}$$

$$\text{HRT} = \frac{V}{Q} = \frac{197.2}{1000} = 0.197\text{ (d)} = 4.73\text{ (h)}$$

**Bước 5 - Tính tỷ phần sinh khối trong bùn hoạt tính và nhu cầu oxy hàng ngày**: Tỷ phần sinh khối dị dưỡng hoạt tính trong $\text{MLVSS}$ đạt $F_{X,\text{act}} = 58.2\%$ (và tổng sinh khối sinh học $A + B$ chiếm $63.5\%$) [Page 23]. Áp dụng phương trình trên Slide $50$ với $P_{X,\text{bio}} = 52.17\text{ kg/d}$ cho nhu cầu oxy tiêu thụ mỗi ngày bằng $R_o = 117.36\text{ kg O}_2/\text{d}$.

$$F_{X,\text{act}} = \frac{A}{P_{X,\text{VSS}}} = \frac{47.86}{82.17} = 0.582 = 58.2\%$$

$$R_o = Q(S_0 - S) - 1.42 P_{X,\text{bio}} = 191.44 - 1.42 \times 52.17 = 117.36\text{ (kg O}_2/\text{d)}$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Nồng độ $\text{bsCOD}$ đầu ra ($S$)**: $0.56\text{ g/m}^3$ (Kiểm tra: $\text{SRT} = 6\text{ d} \gg \text{SRT}_{\min} = \frac{1}{Y k - b} = 0.204\text{ d}\text{ — Đạt chuẩn Slide 42}$)
- **Thể tích bể và thời gian lưu nước ($V, \text{HRT}$)**: $V = 197.2\text{ m}^3$, $\text{HRT} = 0.197\text{ d} = 4.73\text{ h}$ (Kiểm tra: $\frac{V X_T}{\text{SRT}} = \frac{197.2 \times 2.5}{6} = 82.17\text{ kg/d}\text{ — Đạt chuẩn Slide 46}$)
- **Sản lượng bùn hàng ngày ($P_{X,\text{VSS}}, P_{X,\text{TSS}}$)**: $P_{X,\text{VSS}} = 82.17\text{ kg VSS/d}$, $P_{X,\text{TSS}} = 101.37\text{ kg TSS/d}$ (Kiểm tra: $P_{X,\text{TSS}} > P_{X,\text{VSS}}\text{ — Đạt chuẩn Slide 48–49}$)
- **Tỷ phần sinh khối trong $\text{MLVSS}$ ($F_{X,\text{act}}$)**: $58.2\%$ sinh khối hoạt tính và $63.5\%$ tổng sinh khối sinh học (Kiểm tra: $0 < F_{X,\text{act}} < 100\%\text{ — Đạt chuẩn Slide 34, 48}$)
- **Nhu cầu oxy tiêu thụ hàng ngày ($R_o$)**: $117.36\text{ kg O}_2/\text{d}$ (Kiểm tra: $R_o = 191.44 - 74.08 = 117.36\text{ kg O}_2/\text{d}\text{ — Đạt chuẩn Slide 50}$)
