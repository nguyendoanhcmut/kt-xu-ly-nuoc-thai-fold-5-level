### Bài tập ch03_4_ex01 (Slide 18-21, Lời giải từ ảnh chụp slide của thầy): Thiết kế hệ thống tuyển nổi DAF không tuần hoàn và có tuần hoàn nước áp lực

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy]): Thiết kế hệ thống tuyển nổi khí hòa tan (DAF) cho hai phương án không tuần hoàn và có tuần hoàn nước áp lực với lưu lượng trung bình $Q = 400\text{ m}^3/\text{d}$ và nồng độ cặn lơ lửng đầu vào $S_a = 3,000\text{ mg/L}$ [Page 9]. Hệ thống vận hành ở nhiệt độ $T = 20^\circ\text{C}$ có độ hòa tan không khí $s_a = 18.7\text{ mL/L}$, tỷ số khí trên rắn tối ưu $A/S = 0.008\text{ mg/mg}$, áp suất dư tuần hoàn $p = 5\text{ atm}$, hệ số bão hòa $f = 0.5$ và tải trọng bề mặt $\text{SLR} = 100\text{ m}^3/(\text{m}^2\cdot\text{d})$ [Page 9].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng nước thải thiết kế trung bình | $Q$ | $400$ | $\text{m}^3/\text{d}$ (Đề bài Slide $18$) |
| Nồng độ chất rắn lơ lửng đầu vào | $S_a$ | $3,000$ | $\text{mg/L}$ (Đề bài Slide $18$) |
| Tỷ số khí trên rắn tối ưu | $A/S$ | $0.008$ | $\text{mg/mg}$ (Đề bài Slide $18$) |
| Nhiệt độ và độ hòa tan của không khí | $T, s_a$ | $20^\circ\text{C}, 18.7$ | $\text{mL/L}$ (Bảng Slide $14$) |
| Áp suất dư và hệ số bão hòa khí | $p, f$ | $5, 0.5$ | $\text{atm}$, không thứ nguyên (Slide $18$) |
| Tải trọng bề mặt bể tuyển nổi | $\text{SLR}$ | $100$ | $\text{m}^3/(\text{m}^2\cdot\text{d})$ (Đề bài Slide $18$) |
| Tải trọng thủy lực bình áp lực | $\text{HLR}_{\text{vessel}}$ | $1,440$ | $\text{m}^3/(\text{m}^2\cdot\text{d})$ (Bảng Slide $16$) |

**Bước 1 - Tính áp suất bình bão hòa cho phương án không tuần hoàn**: Kỹ sư áp dụng phương trình cân bằng tỷ số khí trên rắn $A/S$ khi không tuần hoàn trên Slide $19$ để xác định áp suất tuyệt đối $P = 3.98\text{ atm}$ [Page 9]. Từ mối liên hệ $P = p + 1$, áp suất dư cần cấp cho bình áp lực đạt $p = 2.98\text{ atm}$ [Page 9].

$$
\frac{A}{S} = \frac{1.3 s_a (f P - 1)}{S_a} \Rightarrow 0.008 = \frac{1.3 \times 18.7 \times (0.5 P - 1)}{3,000}
$$

$$
P = 3.98\text{ atm} = p + 1 \Rightarrow p = 2.98\text{ atm}
$$

**Bước 2 - Tính diện tích bề mặt bể tuyển nổi khi không tuần hoàn**: Diện tích mặt bằng bể tuyển nổi $A_s$ được xác định bằng tỷ số giữa lưu lượng thiết kế $Q$ và tải trọng bề mặt $\text{SLR}$ [Page 9]. Thay số liệu thiết kế vào công thức cho kết quả diện tích bể là $A_s = 4\text{ m}^2$ [Page 9].

$$
A_s = \frac{Q}{\text{SLR}} = \frac{400\text{ m}^3/\text{d}}{100\text{ m}^3/(\text{m}^2\cdot\text{d})} = 4\text{ m}^2
$$

**Bước 3 - Tính áp suất tuyệt đối và lưu lượng dòng tuần hoàn**: Xét phương án có tuần hoàn nước áp lực trên Slide $20$ ở áp suất dư $p = 5\text{ atm}$, áp suất tuyệt đối trong bình đạt $P = 6\text{ atm}$ [Page 9]. Thay vào phương trình cân bằng khí trên rắn có tuần hoàn tìm được lưu lượng tuần hoàn $R = 197\text{ m}^3/\text{d}$ ứng với tỷ lệ tuần hoàn $49.25\%$ [Page 9].

$$
P = p + 1 = 5 + 1 = 6\text{ atm}, \quad \frac{A}{S} = \frac{1.3 s_a (f P - 1) R}{S_a Q}
$$

$$
0.008 = \frac{1.3 \times 18.7 \times (0.5 \times 6 - 1) \times R}{3,000 \times 400} \Rightarrow R = 197\text{ m}^3/\text{d}
$$

**Bước 4 - Tính diện tích bể tuyển nổi và kích thước bình áp lực**: Tổng diện tích bề mặt bể tuyển nổi tính cả lưu lượng tuần hoàn $Q + R$ đạt $A_s = 5.97\text{ m}^2$ và được làm tròn thành $A_s = 6\text{ m}^2$ [Page 9]. Với tải trọng thủy lực bình áp lực chọn từ bảng Slide $16$ là $1,440\text{ m}^3/(\text{m}^2\cdot\text{d})$, tiết diện ngang bình áp lực đạt $A_{\text{vessel}} = 0.137\text{ m}^2$ và đường kính bình đạt $d = 0.42\text{ m}$ [Page 9].

$$
A_s = \frac{Q + R}{\text{SLR}} = \frac{400 + 197}{100} = 5.97\text{ m}^2 \approx 6\text{ m}^2
$$

$$
A_{\text{vessel}} = \frac{197}{1,440} = 0.137\text{ m}^2 \Rightarrow d = \sqrt{\frac{4 \times 0.137}{\pi}} = 0.42\text{ m}
$$

**Bước 5 - Tính tổng lưu lượng không khí nén yêu cầu**: Lưu lượng không khí nén cần cấp cho hệ thống tuyển nổi $Q_{\text{air}}$ được xác định từ tổng lượng chất rắn đầu vào và khối lượng riêng không khí $1.3\text{ g/L}$ trên Slide $21$ [Page 9]. Kết quả tính toán cho lưu lượng khí nén là $Q_{\text{air}} = 7,384.6\text{ L/d}$, tương đương $5.13\text{ L/min}$ [Page 9].

$$
Q_{\text{air}} = \frac{(A/S) \times S_a \times Q}{1.3\text{ g/L}} = \frac{0.008 \times 3,000 \times 400}{1.3} = 7,384.6\text{ L/d} = 5.13\text{ L/min}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Hệ thống tuyển nổi đảm bảo tỷ lệ tuần hoàn và tải trọng bình áp lực nằm trong vùng vận hành tối ưu [Page 8] [Page 9].

- **Áp suất bình bão hòa không tuần hoàn ($P, p$)**: $P = 3.98\text{ atm}$, $p = 2.98\text{ atm}$ (Kiểm tra: $P \in [3.4, 4.8]\text{ atm}\text{ — Đạt chuẩn Slide }5, 19$)
- **Diện tích bể tuyển nổi không tuần hoàn ($A_s$)**: $4\text{ m}^2$ (Kiểm tra: $\text{SLR} = 100\text{ m}^3/(\text{m}^2\cdot\text{d}) \in [80, 240]\text{ m}^3/(\text{m}^2\cdot\text{d})\text{ — Đạt chuẩn Slide }16$)
- **Lưu lượng và tỷ lệ nước tuần hoàn ($R, R/Q$)**: $R = 197\text{ m}^3/\text{d}$, $R/Q = 49.25\%$ (Kiểm tra: $R/Q \in [15\%, 120\%]\text{ — Đạt chuẩn Slide }16, 20$)
- **Diện tích bể tuyển nổi có tuần hoàn ($A_s$)**: $5.97\text{ m}^2 \rightarrow \text{chọn }6\text{ m}^2$ (Kiểm tra: $\text{SLR}_{\text{thực}} = 99.5\text{ m}^3/(\text{m}^2\cdot\text{d})\text{ — Đạt chuẩn Slide }20$)
- **Kích thước bình áp lực ($A_{\text{vessel}}, d$)**: $A_{\text{vessel}} = 0.137\text{ m}^2$, $d = 0.42\text{ m}$ (Kiểm tra: $\text{HLR}_{\text{vessel}} = 1,440\text{ m}^3/(\text{m}^2\cdot\text{d}) \in [1,440, 1,920]\text{ m}^3/(\text{m}^2\cdot\text{d})\text{ — Đạt chuẩn Slide }16, 21$)
- **Lưu lượng khí nén yêu cầu ($Q_{\text{air}}$)**: $7,384.6\text{ L/d} = 5.13\text{ L/min}$ (Kiểm tra: $A/S = 0.008\text{ mg/mg} \in [0.005, 0.06]\text{ mg/mg}\text{ — Đạt chuẩn Slide }16, 21$)

### Bài tập proj_ch03_4_hw01 (Slide 22, Lời giải khôi phục theo chuẩn slide của thầy): So sánh hệ thống tuyển nổi khí hòa tan (DAF) và bể lắng trọng lực theo 5 tiêu chí

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Đối chiếu công nghệ tuyển nổi khí hòa tan (DAF) với công nghệ lắng trọng lực truyền thống (gravity sedimentation) theo $5$ thông số kỹ thuật gồm (a) thời gian lưu nước $\text{HRT}$, (b) tải trọng bề mặt $\text{SLR}$, (c) công suất tiêu thụ năng lượng $P_{\text{input}}$, (d) hiệu suất xử lý $E_{\text{SS}}$, và (e) phạm vi ứng dụng thuận lợi nhất [Page 3] [Page 8]. Phân tích dựa trên số liệu thiết kế chuẩn tại Slide $6, 15, 16$ của Chương $3.4$ và Slide $22$ của Chương $3.3$ [Page 3] [Page 8].

| Tiêu chí kỹ thuật | Ký hiệu / Thông số | Phương án 1 (Tuyển nổi khí hòa tan DAF) | Phương án 2 (Bể lắng trọng lực sơ cấp) |
| :--- | :--- | :--- | :--- |
| (a) Thời gian lưu nước | $\text{HRT}$ | $20 - 30\text{ min}$ (bể DAF) và $1 - 3\text{ min}$ (bình áp lực) | $1.5 - 2.5\text{ h}$, điển hình $2.0\text{ h}$ ($120\text{ min}$) |
| (b) Tải trọng bề mặt | $\text{SLR}$ | $80 - 240\text{ m}^3/(\text{m}^2\cdot\text{d})$, điển hình $100\text{ m}^3/(\text{m}^2\cdot\text{d})$ | $30 - 50\text{ m}^3/(\text{m}^2\cdot\text{d})$, điển hình $40\text{ m}^3/(\text{m}^2\cdot\text{d})$ |
| (c) Tiêu thụ năng lượng | $P_{\text{input}}, P$ | Cao do bơm cao áp $3.4 - 6.0\text{ atm}$ và máy nén khí | Rất thấp, chỉ cấp điện cho dàn gạt bùn đáy quay chậm |
| (d) Hiệu suất khử và độ đặc bùn | $E_{\text{SS}}, C_{\text{sludge}}$ | Khử đến $99\%\text{ SS}$, độ đặc bùn nổi $2 - 3\%\text{ TS}$ | Khử $50 - 70\%\text{ SS}$ lắng được, không tách được hạt nhẹ |
| (e) Phạm vi ứng dụng tối ưu | $\rho_p, \text{FOGs}$ | Nước thải giàu dầu mỡ ($\text{FOGs}$), cặn nhẹ, tảo, nén bùn | Nước thải đô thị chứa hạt cặn thô, tỷ trọng lớn ($\rho_p > \rho_w$) |

**Bước 1 - So sánh thời gian lưu nước và thể tích công trình (Tiêu chí a)**: Hệ thống tuyển nổi DAF chỉ cần thời gian lưu nước $\text{HRT}_{\text{DAF}}$ từ $20\text{ đến }30\text{ min}$ trong bể tuyển nổi và từ $1\text{ đến }3\text{ min}$ trong bình bão hòa áp lực [Page 8]. Ngược lại, bể lắng sơ cấp trọng lực đòi hỏi thời gian lưu nước $\text{HRT}_{\text{sed}}$ từ $1.5\text{ đến }2.5\text{ h}$ (điển hình $2.0\text{ h} = 120\text{ min}$), nên thể tích bể DAF nhỏ hơn từ $4\text{ đến }6$ lần ở cùng lưu lượng $Q$ [Page 8].

$$
\frac{V_{\text{sed}}}{V_{\text{DAF}}} = \frac{\text{HRT}_{\text{sed}}}{\text{HRT}_{\text{DAF}}} = \frac{120\text{ min}}{20\text{ đến }30\text{ min}} = 4.0\text{ đến }6.0
$$

**Bước 2 - So sánh tải trọng bề mặt và diện tích mặt bằng (Tiêu chí b)**: Nhờ lực đẩy nổi của bọt khí mịn đường kính $10\text{ đến }100\text{ }\mu\text{m}$, bể DAF vận hành ở tải trọng bề mặt $\text{SLR}_{\text{DAF}}$ từ $80\text{ đến }240\text{ m}^3/(\text{m}^2\cdot\text{d})$ so với mức $\text{SLR}_{\text{sed}}$ từ $30\text{ đến }50\text{ m}^3/(\text{m}^2\cdot\text{d})$ của bể lắng trọng lực [Page 8]. Tỷ số diện tích mặt bằng yêu cầu giúp công trình DAF tiết kiệm từ $60\%\text{ đến }80\%$ quỹ đất xây dựng [Page 3] [Page 8].

$$
\frac{A_{s,\text{DAF}}}{A_{s,\text{sed}}} = \frac{\text{SLR}_{\text{sed}}}{\text{SLR}_{\text{DAF}}} = \frac{40\text{ m}^3/(\text{m}^2\cdot\text{d})}{100\text{ đến }240\text{ m}^3/(\text{m}^2\cdot\text{d})} = 0.17\text{ đến }0.40
$$

**Bước 3 - So sánh tiêu thụ năng lượng, hiệu suất và phạm vi ứng dụng (Tiêu chí c, d, e)**: Hệ thống DAF tiêu thụ điện năng lớn để duy trì áp suất bình bão hòa $P$ từ $3.4\text{ đến }6.0\text{ atm}$ theo phương trình tỷ số khí trên rắn $A/S$, nhưng đạt hiệu suất khử cặn lơ lửng lên tới $99\%$ và độ đặc bùn nổi từ $2\text{ đến }3\%$ [Page 3] [Page 9]. Vì vậy, bể DAF là lựa chọn tối ưu cho nước thải chứa dầu mỡ ($\text{FOGs}$), bông cặn nhẹ hoặc nén bùn hoạt tính dư, trong khi bể lắng trọng lực phù hợp với cặn nặng có chi phí điện năng tối thiểu [Page 2] [Page 3].

$$
\frac{A}{S} = \frac{1.3 s_a (f P - 1) R}{S_a Q} \in [0.005, 0.06]\text{ mg/mg}, \quad E_{\text{SS,DAF}} \le 99\%
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Bảng đối chiếu làm rõ sự đánh đổi giữa diện tích mặt bằng, hiệu suất tách hạt nhẹ và chi phí năng lượng [Page 3] [Page 8].

- **Thời gian lưu nước ($\text{HRT}$)**: $\text{HRT}_{\text{DAF}} = 20 - 30\text{ min} < \text{HRT}_{\text{sed}} = 90 - 150\text{ min}$ (Kiểm tra: $\text{Giảm }4 - 6\text{ lần thể tích bể — Đạt chuẩn Slide }15$)
- **Tải trọng bề mặt ($\text{SLR}$)**: $\text{SLR}_{\text{DAF}} = 80 - 240\text{ m}^3/(\text{m}^2\cdot\text{d}) > \text{SLR}_{\text{sed}} = 30 - 50\text{ m}^3/(\text{m}^2\cdot\text{d})$ (Kiểm tra: $\text{Tăng }2 - 6\text{ lần tải trọng bề mặt — Đạt chuẩn Slide }16$)
- **Công suất tiêu thụ năng lượng ($P_{\text{input}}$)**: $\text{DAF cao } (P = 3.4 - 6.0\text{ atm}) > \text{Bể lắng thấp}$ (Kiểm tra: $\text{Cần bơm tuần hoàn cao áp và máy nén khí — Đạt chuẩn Slide }5, 6$)
- **Hiệu suất khử cặn và độ đặc bùn ($E_{\text{SS}}, C_{\text{sludge}}$)**: $E_{\text{SS,DAF}} \le 99\%, C_{\text{sludge}} = 2 - 3\%\text{ TS}$ (Kiểm tra: $\text{Vượt trội so với lắng trọng lực }50 - 70\%\text{ — Đạt chuẩn Slide }6, 17$)
- **Phạm vi ứng dụng thuận lợi nhất ($\text{Application}$)**: $\text{DAF tách FOGs, hạt nhẹ, tảo; Bể lắng tách hạt nặng}$ (Kiểm tra: $\text{Phân loại đúng bản chất cơ lý — Đạt chuẩn Slide }3, 6$)

### Bài tập proj_ch03_4_hw02 (Slide 23, Lời giải khôi phục theo chuẩn slide của thầy): Thiết kế hệ thống tuyển nổi DAF có tuần hoàn nước áp lực công suất 4,000 m³/ngày

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Thiết kế hệ thống tuyển nổi khí hòa tan (DAF) có tuần hoàn nước áp lực cho nhà máy có lưu lượng trung bình $Q = 4,000\text{ m}^3/\text{d}$ và nồng độ chất rắn lơ lửng đầu vào $S_a = 1,000\text{ mg/L}$ [Page 9]. Hệ thống vận hành với tỷ số khí trên rắn tối ưu $A/S = 0.015\text{ mg/mg}$, nhiệt độ $T = 20^\circ\text{C}$ ($s_a = 18.7\text{ mL/L}$), áp suất hệ thống tuần hoàn $p = 5\text{ atm}$, hệ số bão hòa $f = 0.5$ và tải trọng bề mặt $\text{SLR} = 100\text{ m}^3/(\text{m}^2\cdot\text{d})$ để xác định (a) tỷ lệ tuần hoàn, (b) diện tích mặt bằng bể và (c) lưu lượng khí nén yêu cầu [Page 7] [Page 8] [Page 9].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng nước thải thiết kế trung bình | $Q$ | $4,000$ | $\text{m}^3/\text{d}$ (Đề bài Slide $23$) |
| Nồng độ chất rắn lơ lửng đầu vào | $S_a$ | $1,000$ | $\text{mg/L}$ (Đề bài Slide $23$) |
| Tỷ số khí trên rắn tối ưu | $A/S$ | $0.015$ | $\text{mg/mg}$ (Đề bài Slide $23$) |
| Nhiệt độ và độ hòa tan không khí | $T, s_a$ | $20^\circ\text{C}, 18.7$ | $\text{mL/L}$ (Bảng Slide $14$) |
| Áp suất dư và áp suất tuyệt đối | $p, P$ | $5, 6$ | $\text{atm}$ ($P = p + 1$, chuẩn Slide $20$) |
| Hệ số bão hòa khí trong bình áp lực | $f$ | $0.5$ | Không thứ nguyên (Đề bài Slide $23$) |
| Tải trọng bề mặt bể tuyển nổi | $\text{SLR}$ | $100$ | $\text{m}^3/(\text{m}^2\cdot\text{d})$ (Đề bài Slide $23$) |

**Bước 1 - Xác định lưu lượng tuần hoàn và tỷ lệ tuần hoàn (Câu a)**: Áp dụng quy ước áp suất trên Slide $20$ của TS. Nguyễn Hoàng Dũng với $P = p + 1 = 6\text{ atm}$, kỹ sư giải phương trình cân bằng $A/S$ có tuần hoàn và thu được lưu lượng tuần hoàn $R = 1,234\text{ m}^3/\text{d}$ [Page 7] [Page 9]. Tỷ lệ tuần hoàn tương ứng đạt $R/Q = 30.85\%$ (hoặc nếu tính theo áp suất tuyệt đối $P = 5\text{ atm}$ thì $R = 1,645.4\text{ m}^3/\text{d}$ và $R/Q = 41.14\%$) [Page 8] [Page 9].

$$
P = p + 1 = 5 + 1 = 6\text{ atm}, \quad \frac{A}{S} = \frac{1.3 s_a (f P - 1) R}{S_a Q}
$$

$$
R = \frac{0.015 \times 1,000 \times 4,000}{1.3 \times 18.7 \times (0.5 \times 6 - 1)} = \frac{60,000}{48.62} = 1,234\text{ m}^3/\text{d}
$$

$$
\text{Tỷ lệ tuần hoàn} = \frac{R}{Q} = \frac{1,234\text{ m}^3/\text{d}}{4,000\text{ m}^3/\text{d}} = 0.3085 = 30.85\%
$$

**Bước 2 - Xác định diện tích bề mặt bể tuyển nổi và bình áp lực (Câu b)**: Tổng diện tích bề mặt bể tuyển nổi $A_s$ tính theo tổng lưu lượng $Q + R$ chia cho tải trọng bề mặt $\text{SLR}$ đạt $52.34\text{ m}^2$ và được chọn tròn là $A_s = 53\text{ m}^2$ [Page 9]. Nếu kiểm tra thêm bình áp lực ở tải trọng $1,440\text{ m}^3/(\text{m}^2\cdot\text{d})$, tiết diện bình đạt $A_{\text{vessel}} = 0.857\text{ m}^2$ ứng với đường kính $d = 1.04\text{ m}$ [Page 8] [Page 9].

$$
A_s = \frac{Q + R}{\text{SLR}} = \frac{4,000 + 1,234}{100} = 52.34\text{ m}^2 \rightarrow \text{Chọn } A_s = 53\text{ m}^2
$$

$$
A_{\text{vessel}} = \frac{1,234}{1,440} = 0.857\text{ m}^2 \Rightarrow d = \sqrt{\frac{4 \times 0.857}{\pi}} = 1.04\text{ m}
$$

**Bước 3 - Xác định lưu lượng không khí nén yêu cầu (Câu c)**: Theo công thức trên Slide $21$ và hướng dẫn đổi đơn vị trên bảng phấn của thầy, tổng khối lượng khí cần cấp đạt $60,000\text{ g/d}$ chia cho khối lượng riêng không khí $1.3\text{ g/L}$ [Page 9]. Lưu lượng khí nén yêu cầu đạt $Q_{\text{air}} = 46,153.8\text{ L/d}$, tương đương $46.15\text{ m}^3/\text{d}$ hoặc $32.05\text{ L/min}$ [Page 9].

$$
Q_{\text{air}} = \frac{(A/S) \times S_a \times Q}{1.3\text{ g/L}} = \frac{0.015 \times 1,000 \times 4,000}{1.3} = 46,153.8\text{ L/d}
$$

$$
Q_{\text{air}} = 46.15\text{ m}^3/\text{d} = \frac{46,153.8\text{ L/d}}{1,440\text{ min/d}} = 32.05\text{ L/min}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Các đại lượng lưu lượng tuần hoàn, diện tích bể và lượng khí cấp đều nằm trong khoảng khuyến nghị của Chương $3.4$ [Page 8] [Page 9].

- **Lưu lượng nước tuần hoàn ($R$)**: $1,234\text{ m}^3/\text{d}$ (hoặc $1,645.4\text{ m}^3/\text{d}$ khi lấy $P = 5\text{ atm}$ tuyệt đối) (Kiểm tra: $P = 6\text{ atm}\text{ — Đạt chuẩn Slide }20$)
- **Tỷ lệ tuần hoàn ($R/Q$)**: $30.85\%$ (hoặc $41.14\%$ khi lấy $P = 5\text{ atm}$ tuyệt đối) (Kiểm tra: $R/Q \in [15\%, 120\%]\text{ — Đạt chuẩn Slide }16$)
- **Diện tích bề mặt bể tuyển nổi ($A_s$)**: $52.34\text{ m}^2 \rightarrow \text{chọn }53\text{ m}^2$ (Kiểm tra: $\text{SLR} = 100\text{ m}^3/(\text{m}^2\cdot\text{d}) \in [80, 240]\text{ m}^3/(\text{m}^2\cdot\text{d})\text{ — Đạt chuẩn Slide }16$)
- **Kích thước bình bão hòa áp lực ($A_{\text{vessel}}, d$)**: $A_{\text{vessel}} = 0.857\text{ m}^2$, $d = 1.04\text{ m}$ (Kiểm tra: $\text{HLR}_{\text{vessel}} = 1,440\text{ m}^3/(\text{m}^2\cdot\text{d}) \in [1,440, 1,920]\text{ m}^3/(\text{m}^2\cdot\text{d})\text{ — Đạt chuẩn Slide }16$)
- **Lưu lượng không khí nén yêu cầu ($Q_{\text{air}}$)**: $46,153.8\text{ L/d} = 46.15\text{ m}^3/\text{d} = 32.05\text{ L/min}$ (Kiểm tra: $A/S = 0.015\text{ mg/mg} \in [0.005, 0.06]\text{ mg/mg}\text{ — Đạt chuẩn Slide }16, 21$)
