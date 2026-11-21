### Bài tập ch04_2_ex01 (Slide 21–25, Ảnh #63–#66): Thiết kế Bể Tạo bông Dùng Tuabin Trục đứng 3 Ngăn Nối tiếp

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy]): Thiết kế bể tạo bông dùng tuabin trục đứng gồm $N_{\text{stage}} = 3\text{ ngăn}$ nối tiếp cho nhà máy xử lý nước thải có lưu lượng $Q = 9,000\text{ m}^3\text{/ngày}$ và thời gian lưu nước tổng cộng $t = 30\text{ phút}$ [Page 11]. Tại nhiệt độ vận hành $T = 20^\circ\text{C}$, nước thải có khối lượng riêng $\rho = 998.2\text{ kg/m}^3$ và độ nhớt động lực học $\mu$ bằng $1.002 \times 10^{-3}\text{ Pa}\cdot\text{s}$ [Page 11].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng thiết kế | $Q$ | $9,000$ | $\text{m}^3\text{/ngày}$ (Slide $21$) |
| Thời gian lưu nước tổng cộng | $t$ | $30$ | $\text{phút}$ (Slide $21$) |
| Số bậc ngăn tạo bông nối tiếp | $N_{\text{stage}}$ | $3$ | $\text{ngăn}$ (Slide $21$) |
| Khối lượng riêng của nước ở $20^\circ\text{C}$ | $\rho$ | $998.2$ | $\text{kg/m}^3$ (Slide $21$) |
| Độ nhớt động lực học ở $20^\circ\text{C}$ | $\mu$ | $1.002 \times 10^{-3}$ | $\text{Pa}\cdot\text{s}$ (Slide $21$) |
| Kích thước mặt bằng mỗi ngăn chọn | $L \times W$ | $4 \times 4$ | $\text{m} \times \text{m}$ (Slide $16, 23$) |
| Chiều cao bảo vệ chọn | $H_{\text{fb}}$ | $0.6$ | $\text{m}$ (Slide $23$) |
| Loại cánh khuấy chọn | $\text{Hydrofoil}$ | $3\text{ cánh}$ | $\text{Cánh nghiêng}$ (Slide $16, 23$) |
| Vị trí đặt cánh khuấy dưới mặt nước | $h_{\text{imp}}$ | $\frac{2}{3}D_{\text{tank}}$ | $\text{m}$ (Slide $16, 23$) |
| Tỷ số đường kính cánh khuấy chọn | $D/T_e$ | $0.4$ | $\text{Không thứ nguyên}$ (Slide $20$) |
| Tốc độ quay cánh khuấy ngăn đầu | $N$ | $30$ ($0.5$) | $\text{vòng/phút}$ ($\text{vòng/s}$, Slide $20$) |
| Chuẩn số công suất cánh hydrofoil | $N_p$ | $0.3$ | $\text{Không thứ nguyên}$ (Slide $16$) |
| Chuẩn số bơm cánh hydrofoil | $N_Q$ | $0.5$ | $\text{Không thứ nguyên}$ (Slide $16$) |

**Bước 1 - Tính tổng thể tích bể tạo bông và thể tích mỗi ngăn**: Từ lưu lượng $Q = 9,000\text{ m}^3\text{/ngày}$ và thời gian lưu $t = 30\text{ phút}$, ta xác định tổng thể tích bể đạt $V_{\text{total}} = 187.5\text{ m}^3$ và thể tích mỗi ngăn trong $3\text{ ngăn}$ nối tiếp đạt $V_{\text{chamber}} = 62.5\text{ m}^3$ [Page 11].

$$
V_{\text{total}} = \frac{Q \times t}{1,440} = \frac{9,000 \times 30}{1,440} = 187.5\text{ (m}^3\text{)}
$$

$$
V_{\text{chamber}} = \frac{V_{\text{total}}}{N_{\text{stage}}} = \frac{187.5}{3} = 62.5\text{ (m}^3\text{)}
$$

**Bước 2 - Tính kích thước hình học ngăn bể và vị trí lắp đặt cánh khuấy**: Khi chọn mặt bằng hình vuông có $L = 4\text{ m}$ và $W = 4\text{ m}$ cùng chiều cao bảo vệ $H_{\text{fb}} = 0.6\text{ m}$, chiều sâu nước đạt $D_{\text{tank}} = 3.9\text{ m}$, tổng chiều cao bể đạt $H_{\text{tank}} = 4.5\text{ m}$ và vị trí đặt cánh khuấy nằm ở độ sâu $h_{\text{imp}} = 2.6\text{ m}$ dưới mặt nước (cách đáy bể $1.3\text{ m}$) [Page 8] [Page 10].

$$
D_{\text{tank}} = \frac{V_{\text{chamber}}}{L \times W} = \frac{62.5}{4 \times 4} = 3.9\text{ (m)}
$$

$$
H_{\text{tank}} = 3.9 + 0.6 = 4.5\text{ (m)}, \quad h_{\text{imp}} = \frac{2}{3} \times 3.9 = 2.6\text{ (m)}
$$

**Bước 3 - Tính đường kính tương đương mặt bằng và đường kính cánh khuấy**: Từ diện tích mặt bằng ngăn bể $A_{\text{plan}} = 16\text{ m}^2$, đường kính tương đương của ngăn bể đạt $T_e = 4.5\text{ m}$ và đường kính cánh khuấy theo tỷ số ưu tiên $D/T_e = 0.4$ đạt $D = 1.8\text{ m}$ [Page 10].

$$
T_e = \sqrt{\frac{4 \times A_{\text{plan}}}{\pi}} = \sqrt{\frac{4 \times 4 \times 4}{3.14}} = 4.5\text{ (m)}
$$

$$
D = 0.4 \times T_e = 0.4 \times 4.5 = 1.8\text{ (m)}
$$

**Bước 4 - Kiểm tra chuẩn số Reynolds và vận tốc dài ở đầu cánh khuấy**: Với tốc độ quay ở ngăn đầu tiên chọn là $N = 30\text{ vòng/phút}$ (tức $0.5\text{ vòng/s}$), chuẩn số Reynolds đạt $\text{Re} = 1,613,856 > 10,000$ và vận tốc đầu cánh đạt $v_{\text{tip}} = 2.8\text{ m/s}$ thỏa mãn tiêu chuẩn thiết kế [Page 9] [Page 10].

$$
\text{Re} = \frac{D^2 \times N \times \rho}{\mu} = \frac{1.8^2 \times 0.5 \times 998.2}{1.002 \times 10^{-3}} = 1,613,856 > 10,000
$$

$$
v_{\text{tip}} = N \times \pi \times D = 0.5 \times \pi \times 1.8 = 2.8\text{ (m/s)}
$$

**Bước 5 - Tính công suất khuấy trộn và kiểm tra gradien vận tốc**: Áp dụng chuẩn số công suất $N_p = 0.3$ cho cánh khuấy hydrofoil $3\text{ cánh}$, công suất khuấy yêu cầu ở ngăn đầu tiên đạt $P = 707\text{ W}$ và tạo ra gradien vận tốc trung bình đạt $G = 106\text{ s}^{-1}$ [Page 8] [Page 9].

$$
P = N_p \times \rho \times N^3 \times D^5 = 0.3 \times 998.2 \times 0.5^3 \times 1.8^5 = 707\text{ (W)}
$$

$$
G = \sqrt{\frac{P}{\mu \times V_{\text{chamber}}}} = \sqrt{\frac{707}{1.002 \times 10^{-3} \times 62.5}} = 106\text{ (s}^{-1}\text{)}
$$

**Bước 6 - Tính lưu lượng tuần hoàn qua cánh khuấy và thời gian một vòng tuần hoàn**: Với chuẩn số bơm $N_Q = 0.5$, lưu lượng dòng chảy do cánh khuấy tạo ra đạt $Q_{\text{imp}} = 1.46\text{ m}^3\text{/s}$ và thời gian tuần hoàn toàn bộ thể tích ngăn bể đạt $t_c = 42.8\text{ s}$ [Page 9].

$$
Q_{\text{imp}} = N_Q \times N \times D^3 = 0.5 \times 0.5 \times 1.8^3 = 1.46\text{ (m}^3\text{/s)}
$$

$$
t_c = \frac{V_{\text{chamber}}}{Q_{\text{imp}}} = \frac{62.5}{1.46} = 42.8\text{ (s)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Tổng thể tích bể tạo bông ($V_{\text{total}}$)**: $187.5\text{ m}^3$ cho $3\text{ ngăn}$, mỗi ngăn $V_{\text{chamber}} = 62.5\text{ m}^3$ (Kiểm tra: $t = 30\text{ phút} \in [30, 60]\text{ phút — Đạt chuẩn Slide } 14$).
- **Kích thước mỗi ngăn bể ($L \times W \times D_{\text{tank}}$)**: $4\text{ m} \times 4\text{ m} \times 3.9\text{ m}$, cao $H_{\text{tank}} = 4.5\text{ m}$ (Kiểm tra: $L/W = 1.0 \in [1.0, 1.25]\text{ — Đạt chuẩn Slide } 16, 20$).
- **Đường kính cánh khuấy hydrofoil ($D$)**: $1.8\text{ m}$ đặt sâu $h_{\text{imp}} = 2.6\text{ m}$, cách đáy $1.3\text{ m}$ (Kiểm tra: $D/T_e = 0.4 \in [0.3, 0.6]\text{ — Đạt chuẩn Slide } 20$).
- **Chuẩn số Reynolds ($\text{Re}$)**: $1,613,856$ tại tốc độ quay $N = 30\text{ vòng/phút}$ (Kiểm tra: $\text{Re} = 1,613,856 > 10,000\text{ — Đạt chuẩn Slide } 17, 24$).
- **Vận tốc dài ở đầu cánh khuấy ($v_{\text{tip}}$)**: $2.8\text{ m/s}$ (Kiểm tra: $v_{\text{tip}} = 2.8\text{ m/s} \in [2.0, 3.0]\text{ m/s — Đạt chuẩn Slide } 20, 24$).
- **Công suất khuấy và gradien vận tốc ngăn đầu ($P, G$)**: $P = 707\text{ W}$ và $G = 106\text{ s}^{-1}$ (Kiểm tra: $G = 106\text{ s}^{-1}\text{ cấp đầu vào — Đạt chuẩn Slide } 6, 25$).
- **Lưu lượng bơm và chu kỳ tuần hoàn ($Q_{\text{imp}}, t_c$)**: $Q_{\text{imp}} = 1.46\text{ m}^3\text{/s}$ và $t_c = 42.8\text{ s}$ (Kiểm tra: $t_c = 42.8\text{ s} \ll 600\text{ s — Đạt chuẩn Slide } 18, 25$).

### Bài tập ch04_2_ex02 (Slide 32–39, Ảnh #67–#73 và #116–#130): Thiết kế Bể Tạo bông Dùng Guồng Khuấy Trục ngang 3 Ngăn Nối tiếp

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy]): Thiết kế bể tạo bông dùng guồng khuấy trục ngang gồm $N_{\text{stage}} = 3\text{ ngăn}$ nối tiếp cho lưu lượng $Q = 54,000\text{ m}^3\text{/ngày}$ và thời gian lưu nước $t = 30\text{ phút}$ [Page 14]. Mỗi tay guồng lắp $3\text{ thanh}$ cánh khuấy có mép ngoài đặt cách tâm trục quay tại các bán kính $r_1 = 0.67\text{ m}$, $r_2 = 1.33\text{ m}$ và $r_3 = 2.0\text{ m}$ [Page 14]. Tại nhiệt độ $T = 20^\circ\text{C}$, nước có khối lượng riêng $\rho = 998.2\text{ kg/m}^3$ và độ nhớt động lực học $\mu$ bằng $1.002 \times 10^{-3}\text{ Pa}\cdot\text{s}$ [Page 14].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng thiết kế | $Q$ | $54,000$ | $\text{m}^3\text{/ngày}$ (Slide $32$) |
| Thời gian lưu nước tổng cộng | $t$ | $30$ | $\text{phút}$ (Slide $32$) |
| Số bậc ngăn tạo bông nối tiếp | $N_{\text{stage}}$ | $3$ | $\text{ngăn}$ (Slide $32$) |
| Bán kính mép ngoài $3\text{ thanh}$ cánh | $r_1, r_2, r_3$ | $0.67;\; 1.33;\; 2.0$ | $\text{m}$ (Slide $31, 32$) |
| Khối lượng riêng của nước ở $20^\circ\text{C}$ | $\rho$ | $998.2$ | $\text{kg/m}^3$ (Slide $32$) |
| Độ nhớt động lực học ở $20^\circ\text{C}$ | $\mu$ | $1.002 \times 10^{-3}$ | $\text{Pa}\cdot\text{s}$ (Slide $32$) |
| Khoảng hở từ guồng đến thành bể | $c_{\text{wall}}$ | $0.7$ | $\text{m}$ (Slide $30$) |
| Khoảng cách giữa hai guồng trên trục | $c_{\text{wheel}}$ | $1.0$ | $\text{m}$ (Slide $30$) |
| Độ sâu nước tăng thêm ngoài guồng | $\Delta D$ | $1.0$ | $\text{m}$ (Slide $30$) |
| Chiều cao bảo vệ chọn | $H_{\text{fb}}$ | $0.5$ | $\text{m}$ (Slide $34$) |
| Bề rộng bản thanh gỗ cánh khuấy | $w_p$ | $0.15$ | $\text{m}$ (Slide $30$: $100 \times 150\text{ mm}$) |
| Số tay khuấy trên mỗi guồng khuấy | $N_{\text{arm}}$ | $4$ | $\text{tay/guồng}$ (Slide $31, 37$) |
| Hệ số cản thủy động thanh cánh dài | $C_d$ | $1.9$ | $\text{Không thứ nguyên}$ (Slide $30$) |
| Tốc độ quay trục guồng khuấy chọn | $N$ | $2.1$ ($0.035$) | $\text{vòng/phút}$ ($\text{vòng/s}$, Slide $30$) |

**Bước 1 - Tính tổng thể tích bể tạo bông và thể tích mỗi ngăn**: Từ lưu lượng $Q = 54,000\text{ m}^3\text{/ngày}$ và thời gian lưu $t = 30\text{ phút}$, tổng thể tích bể tạo bông đạt $V_{\text{total}} = 1,125\text{ m}^3$ và thể tích mỗi ngăn trong $3\text{ ngăn}$ nối tiếp đạt $V_{\text{chamber}} = 375\text{ m}^3$ [Page 14].

$$
V_{\text{total}} = \frac{Q \times t}{1,440} = \frac{54,000 \times 30}{1,440} = 1,125\text{ (m}^3\text{)}
$$

$$
V_{\text{chamber}} = \frac{V_{\text{total}}}{N_{\text{stage}}} = \frac{1,125}{3} = 375\text{ (m}^3\text{)}
$$

**Bước 2 - Tính đường kính guồng khuấy và kích thước hình học của mỗi ngăn**: Đường kính ngoài của guồng khuấy bằng hai lần bán kính $r_3 = 2.0\text{ m}$ nên đạt $D_{\text{wheel}} = 4\text{ m}$ [Page 13] [Page 14]. Cộng khoảng hở thành bể $0.7\text{ m}$ mỗi bên và chiều sâu vượt đường kính guồng $1.0\text{ m}$, mỗi ngăn có chiều dài $L_c = 5.4\text{ m}$, chiều sâu nước $D_c = 5\text{ m}$ (cao $H_c = 5.5\text{ m}$) và chiều rộng $W_c = 13.9\text{ m}$ [Page 13].

$$
D_{\text{wheel}} = 2 \times r_3 = 2 \times 2 = 4\text{ (m)}, \quad L_c = 4 + (2 \times 0.7) = 5.4\text{ (m)}
$$

$$
D_c = 4 + 1 = 5\text{ (m)}, \quad H_c = 5 + 0.5 = 5.5\text{ (m)}
$$

$$
W_c = \frac{V_{\text{chamber}}}{L_c \times D_c} = \frac{375}{5.4 \times 5} = 13.9\text{ (m)}
$$

**Bước 3 - Thử chọn số lượng guồng khuấy trên trục và chọn lại theo giới hạn chiều dài cánh**: Khi thử chọn $N_{\text{wheel}} = 2\text{ guồng}$, chiều dài mỗi thanh cánh đạt $l_p = 5.75\text{ m}$ vượt quá giới hạn tối đa $3.5\text{ m}$ trên bảng Slide $30$ nên không thỏa mãn [Page 13]. Khi chọn lại $N_{\text{wheel}} = 3\text{ guồng}$ với tổng khoảng hở $c_{\text{req}} = 3.4\text{ m}$, chiều dài mỗi thanh cánh đạt $l_p = 3.5\text{ m}$ thỏa mãn hoàn toàn tiêu chuẩn thiết kế [Page 13].

$$
c_{\text{req,2}} = (2 \times 0.7) + 1 = 2.4\text{ (m)} \implies l_{p,2} = \frac{13.9 - 2.4}{2} = 5.75\text{ (m)} > 3.5\text{ (m)}
$$

$$
c_{\text{req,3}} = (2 \times 0.7) + (2 \times 1) = 3.4\text{ (m)} \implies l_p = \frac{13.9 - 3.4}{3} = 3.5\text{ (m)}
$$

**Bước 4 - Tính diện tích thanh cánh ở mỗi bậc bán kính và vận tốc tương đối của từng thanh cánh**: Với thanh cánh dài $l_p = 3.5\text{ m}$ và rộng $w_p = 0.15\text{ m}$, tỷ số $l_p/w_p = 23.3$ ứng với hệ số cản $C_d = 1.9$ và diện tích cánh ở mỗi vị trí bán kính ($1, 2, 3$) trên $3\text{ guồng}$ đạt $A_p = 6.3\text{ m}^2$ [Page 13]. Ở tốc độ quay $N = 0.035\text{ vòng/s}$, vận tốc dài tại tâm ba thanh cánh lần lượt đạt $v_{R1} = 0.131\text{ m/s}$, $v_{R2} = 0.276\text{ m/s}$, $v_{R3} = 0.423\text{ m/s}$ và vận tốc mép ngoài đạt $v_{\text{tip}} = 0.44\text{ m/s}$ [Page 13].

$$
\frac{l_p}{w_p} = \frac{3.5}{0.15} = 23.3 \implies C_d = 1.9, \quad A_p = 3 \times 4 \times (3.5 \times 0.15) = 6.3\text{ (m}^2\text{)}
$$

$$
R_1 = 0.67 - \frac{0.15}{2} = 0.595\text{ (m)} \implies v_{R1} = 0.035 \times 2\pi \times 0.595 = 0.131\text{ (m/s)}
$$

$$
R_2 = 1.33 - \frac{0.15}{2} = 1.255\text{ (m)} \implies v_{R2} = 0.035 \times 2\pi \times 1.255 = 0.276\text{ (m/s)}
$$

$$
R_3 = 2.0 - \frac{0.15}{2} = 1.925\text{ (m)} \implies v_{R3} = 0.035 \times 2\pi \times 1.925 = 0.423\text{ (m/s)}
$$

$$
v_{\text{tip}} = 0.035 \times 2\pi \times 2.0 = 0.44\text{ (m/s)} < 0.5\text{ (m/s)}
$$

**Bước 5 - Tính công suất khuấy trộn và kiểm tra gradien vận tốc, số Reynolds cùng tỷ lệ diện tích cánh**: Tổng công suất khuấy của cả $3\text{ vị trí}$ cánh đạt $P = 591\text{ W}$, tạo ra gradien vận tốc $G = 40\text{ s}^{-1}$ và chuẩn số Reynolds đạt $\text{Re} = 557,876 > 10,000$ [Page 12] [Page 13]. Tổng diện tích mặt quạt cánh khuấy trên một mặt phẳng đứng đạt $A_P = 9.45\text{ m}^2$, chiếm tỷ lệ $13.6\%$ so với diện tích mặt cắt ngang ngăn bể $A_{\text{sec}} = 69.5\text{ m}^2$ [Page 13].

$$
P = \frac{C_d \times A_p \times \rho}{2} \times \left(v_{R1}^3 + v_{R2}^3 + v_{R3}^3\right)
$$

$$
P = \frac{1.9 \times 6.3 \times 998.2}{2} \times \left(0.131^3 + 0.276^3 + 0.423^3\right) = 591\text{ (W)}
$$

$$
G = \sqrt{\frac{P}{\mu \times V_{\text{chamber}}}} = \sqrt{\frac{591}{1.002 \times 10^{-3} \times 375}} = 40\text{ (s}^{-1}\text{)}
$$

$$
\text{Re} = \frac{D_{\text{wheel}}^2 \times N \times \rho}{\mu} = \frac{4^2 \times 0.035 \times 998.2}{1.002 \times 10^{-3}} = 557,876 > 10,000
$$

$$
\frac{A_P}{A_{\text{sec}}} = \frac{3 \times 6 \times (3.5 \times 0.15)}{5 \times 13.9} = \frac{9.45}{69.5} = 13.6\% < 20\%
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Kích thước mỗi ngăn bể ($H_c \times L_c \times W_c$)**: $5.5\text{ m} \times 5.4\text{ m} \times 13.9\text{ m}$, sâu nước $D_c = 5\text{ m}$ (Kiểm tra: $L_c \in [3, 8]\text{ m}, W_c \in [3, 25]\text{ m — Đạt chuẩn Slide } 30, 36$).
- **Cấu hình guồng khuấy ($N_{\text{wheel}}, D_{\text{wheel}}, l_p$)**: $3\text{ guồng/trục}$, đường kính $D_{\text{wheel}} = 4\text{ m}$, cánh dài $l_p = 3.5\text{ m}$ (Kiểm tra: $l_p = 3.5\text{ m} \in [2, 3.5]\text{ m — Đạt chuẩn Slide } 30, 35$).
- **Vận tốc đầu cánh cực đại ($v_{\text{tip}}$)**: $0.44\text{ m/s}$ tại tốc độ quay $N = 2.1\text{ vòng/phút}$ (Kiểm tra: $v_{\text{tip}} = 0.44\text{ m/s} < 0.5\text{ m/s — Đạt chuẩn Slide } 30, 38$).
- **Công suất khuấy và gradien vận tốc ($P, G$)**: $P = 591\text{ W}$ và $G = 40\text{ s}^{-1}$ (Kiểm tra: $G = 40\text{ s}^{-1} \in [5, 40]\text{ s}^{-1}\text{ — Đạt chuẩn Slide } 30, 39$).
- **Chuẩn số Reynolds ($\text{Re}$)**: $557,876$ (Kiểm tra: $\text{Re} = 557,876 > 10,000\text{ — Đạt chuẩn Slide } 28, 39$).
- **Tỷ lệ diện tích cánh trên mặt cắt ngang bể ($A_P/A_{\text{sec}}$)**: $13.6\%$ với $A_P = 9.45\text{ m}^2$ và $A_{\text{sec}} = 69.5\text{ m}^2$ (Kiểm tra: $13.6\% < 20\%\text{ — Đạt chuẩn Slide } 30, 39$).

### Bài tập proj_ch04_2_hw01 (Slide 40–43, Ảnh #74 và #129–#134): Tính toán Chi phí Hóa chất, Bơm Định lượng và Bồn Pha PAC và Polymer Anion

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy]): Một trạm xử lý nước thải có công suất $Q = 1,000\text{ m}^3\text{/ngày}$ vận hành liên tục $24\text{ giờ/ngày}$ [Page 3]. Bằng phương pháp Jartest, liều lượng hóa chất châm vào bể keo tụ là $\text{PAC}$ ở mức $D_{\text{PAC}} = 150\text{ g/m}^3$ (đơn giá $6,000\text{ VND/kg}$, pha dung dịch nồng độ $C_{\text{PAC}} = 7.5\%\text{ m/V}$) và châm vào bể tạo bông là Polymer Anion ở mức $D_{\text{Poly}} = 3\text{ g/m}^3$ (đơn giá $60,000\text{ VND/kg}$, pha dung dịch nồng độ $C_{\text{Poly}} = 0.1\%\text{ m/V}$). Công nhân pha hóa chất $N_{\text{batch}} = 2\text{ lần/ngày}$. Hãy tính chi phí hóa chất trong $1\text{ ngày}$, lưu lượng bơm định lượng ($\text{L/h}$) và dung tích bồn pha hóa chất ($\text{L}$) [Page 3].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng xử lý của nhà máy | $Q$ | $1,000$ | $\text{m}^3\text{/ngày}$ (Slide $40$) |
| Liều lượng hóa chất keo tụ $\text{PAC}$ | $D_{\text{PAC}}$ | $150$ | $\text{g/m}^3$ (Slide $40$) |
| Liều lượng chất trợ keo tụ Polymer Anion | $D_{\text{Poly}}$ | $3$ | $\text{g/m}^3$ (Slide $40$) |
| Đơn giá hóa chất $\text{PAC}$ | $P_{\text{PAC}}$ | $6,000$ | $\text{VND/kg}$ (Slide $40$) |
| Đơn giá hóa chất Polymer Anion | $P_{\text{Poly}}$ | $60,000$ | $\text{VND/kg}$ (Slide $40$) |
| Nồng độ dung dịch $\text{PAC}$ sau pha | $C_{\text{PAC}}$ | $7.5\%$ | $\text{m/V}$ ($\text{kg/100 L}$, Slide $40$) |
| Nồng độ dung dịch Polymer Anion sau pha | $C_{\text{Poly}}$ | $0.1\%$ | $\text{m/V}$ ($\text{kg/100 L}$, Slide $40$) |
| Thời gian bơm vận hành trong ngày | $t_{\text{op}}$ | $24$ | $\text{giờ/ngày}$ (Slide $40$) |
| Số mẻ pha hóa chất mỗi ngày | $N_{\text{batch}}$ | $2$ | $\text{mẻ/ngày}$ (Slide $40$) |

**Bước 1 - Tính khối lượng và tổng chi phí hóa chất PAC và Polymer Anion trong 1 ngày (Câu a)**: Khối lượng bột $\text{PAC}$ dùng trong $1\text{ ngày}$ đạt $M_{\text{PAC}} = 150\text{ kg/ngày}$ (chi phí $900,000\text{ VND/ngày}$) và khối lượng bột Polymer Anion đạt $M_{\text{Poly}} = 3\text{ kg/ngày}$ (chi phí $180,000\text{ VND/ngày}$), suy ra tổng chi phí hóa chất đạt $\text{Cost}_{\text{total}} = 1,080,000\text{ VND/ngày}$ [Page 3].

$$
M_{\text{PAC}} = 150 \times 1,000 \times \frac{1}{1,000} = 150\text{ (kg/ngày)}
$$

$$
\text{Cost}_{\text{PAC}} = 150 \times 6,000 = 900,000\text{ (VND/ngày)}
$$

$$
M_{\text{Poly}} = 3 \times 1,000 \times \frac{1}{1,000} = 3\text{ (kg/ngày)}
$$

$$
\text{Cost}_{\text{Poly}} = 3 \times 60,000 = 180,000\text{ (VND/ngày)}
$$

$$
\text{Cost}_{\text{total}} = 900,000 + 180,000 = 1,080,000\text{ (VND/ngày)}
$$

**Bước 2 - Tính thể tích dung dịch mỗi ngày và lưu lượng bơm định lượng vận hành 24/24 (Câu b)**: Thể tích dung dịch $\text{PAC}$ nồng độ $7.5\%$ cần dùng mỗi ngày là $V_{\text{PAC}} = 2,000\text{ L/ngày}$ ứng với lưu lượng bơm định lượng $Q_{\text{pump,PAC}} = 84\text{ L/h}$, còn thể tích dung dịch Polymer Anion nồng độ $0.1\%$ là $V_{\text{Poly}} = 3,000\text{ L/ngày}$ ứng với lưu lượng bơm $Q_{\text{pump,Poly}} = 125\text{ L/h}$ [Page 3].

$$
V_{\text{PAC}} = \frac{M_{\text{PAC}}}{C_{\text{PAC}}} = \frac{150}{7.5\%} = 2,000\text{ (L/ngày)} \implies Q_{\text{pump,PAC}} = \frac{2,000}{24} = 84\text{ (L/h)}
$$

$$
V_{\text{Poly}} = \frac{M_{\text{Poly}}}{C_{\text{Poly}}} = \frac{3}{0.1\%} = 3,000\text{ (L/ngày)} \implies Q_{\text{pump,Poly}} = \frac{3,000}{24} = 125\text{ (L/h)}
$$

**Bước 3 - Tính thể tích bồn pha hóa chất khi pha 2 lần mỗi ngày (Câu c)**: Do công nhân pha hóa chất $2\text{ lần/ngày}$, thể tích cần thiết mỗi mẻ của bồn $\text{PAC}$ là $V_{\text{tank,PAC}} = 1,000\text{ L}$ và của bồn Polymer Anion là $V_{\text{tank,Poly}} = 1,500\text{ L}$, nên người thiết kế chọn $1\text{ bồn}$ tiêu chuẩn dung tích $1,500\text{ L}$ cho mỗi loại hóa chất [Page 3].

$$
V_{\text{tank,PAC}} = \frac{2,000}{2} = 1,000\text{ (L)}, \quad V_{\text{tank,Poly}} = \frac{3,000}{2} = 1,500\text{ (L)}
$$

$$
V_{\text{tank,chosen}} = \max(1,000;\; 1,500) = 1,500\text{ (L)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Khối lượng và chi phí $\text{PAC}$ hàng ngày ($M_{\text{PAC}}, \text{Cost}_{\text{PAC}}$)**: $150\text{ kg/ngày}$ và $900,000\text{ VND/ngày}$ (Kiểm tra: $M_{\text{PAC}} = 150\text{ kg/ngày — Đạt chuẩn Slide } 41$).
- **Khối lượng và chi phí Polymer Anion hàng ngày ($M_{\text{Poly}}, \text{Cost}_{\text{Poly}}$)**: $3\text{ kg/ngày}$ và $180,000\text{ VND/ngày}$ (Kiểm tra: $D_{\text{Poly}} = 3\text{ mg/L} \in [1, 10]\text{ mg/L — Đạt chuẩn Slide } 6, 41$).
- **Tổng chi phí hóa chất hàng ngày ($\text{Cost}_{\text{total}}$)**: $1,080,000\text{ VND/ngày}$ (Kiểm tra: $900,000 + 180,000 = 1,080,000\text{ VND/ngày — Đạt chuẩn Slide } 41$).
- **Lưu lượng bơm định lượng ($Q_{\text{pump,PAC}}, Q_{\text{pump,Poly}}$)**: Bơm $\text{PAC}$ đạt $84\text{ L/h}$ và bơm Polymer đạt $125\text{ L/h}$ (Kiểm tra: $Q_{\text{pump}} \times 24\text{ h} \ge V_{\text{sol}}\text{ — Đạt chuẩn Slide } 42$).
- **Dung tích bồn pha hóa chất ($V_{\text{tank,chosen}}$)**: Chọn đồng bộ $1\text{ bồn } 1,500\text{ L}$ cho mỗi hóa chất (Kiểm tra: $1,500\text{ L} \ge 1,000\text{ L}, 1,500\text{ L — Đạt chuẩn Slide } 43$).
