### Bài tập ch03_5_ex01 (Slide 13–15, Ảnh chụp lớp học #50–#52): Tính Tổn Thất Áp Lực Qua Tầng Lọc Than Antraxit Sạch

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy] — Ảnh lớp học #50, #51, #52, Slide $13\text{–}15$): Tính tổn thất áp lực qua tầng vật liệu lọc sạch $h_L$ của bể lọc nhanh một lớp than antraxit tầng sâu có chiều dày $L = 1.8\text{ m}$ và đường kính hữu hiệu $\text{ES} = 0.95\text{ mm}$ [Page 7]. Hệ thống vận hành ở vận tốc lọc $v = 15\text{ m/h}$ và nhiệt độ nước đầu vào $T = 15^\circ\text{C}$ [Page 6] [Page 7].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Nhiệt độ nước đầu vào | $T$ | $15$ | $^\circ\text{C}$ (Slide $13$) |
| Khối lượng riêng của nước ở $15^\circ\text{C}$ | $\rho_w$ | $999.1$ | $\text{kg/m}^3$ (Slide $14$, Ảnh #50) |
| Độ nhớt động lực học của nước ở $15^\circ\text{C}$ | $\mu$ | $1.139 \times 10^{-3}$ | $\text{Pa}\cdot\text{s}$ (Slide $14$, Ảnh #50) |
| Chiều dày lớp vật liệu than antraxit | $L$ | $1.8$ | $\text{m}$ (Slide $13$) |
| Đường kính hữu hiệu hạt than antraxit | $d$ | $0.95 \times 10^{-3}$ | $\text{m}$ ($\text{ES} = 0.95\text{ mm}$, Slide $13$) |
| Vận tốc lọc thiết kế | $v$ | $0.004167$ | $\text{m/s}$ ($15\text{ m/h}$, Slide $14$) |
| Hệ số tổn thất áp lực nhớt chọn | $\kappa_V$ | $228$ | $\text{Không thứ nguyên}$ (Dải $210\text{–}245$, Slide $12, 14$) |
| Hệ số tổn thất áp lực quán tính chọn | $\kappa_I$ | $4.4$ | $\text{Không thứ nguyên}$ (Dải $3.5\text{–}5.3$, Slide $12, 14$) |
| Độ rỗng tầng vật liệu lọc tĩnh chọn | $\epsilon$ | $0.50$ | $\text{Không thứ nguyên}$ ($\epsilon = 50\%$, Slide $9, 14$) |
| Gia tốc trọng trường | $g$ | $9.81$ | $\text{m/s}^2$ (Slide $12$) |

**Bước 1 - Quy đổi vận tốc lọc và kiểm tra chuẩn số Reynolds dòng thấm**: Kỹ sư đổi vận tốc lọc từ $v = 15\text{ m/h}$ sang đơn vị chuẩn là $v = 0.004167\text{ m/s}$ trên Slide $14$ [Page 6] [Page 7]. Chuẩn số Reynolds của dòng chảy qua lớp hạt than antraxit đạt $\text{Re} = 3.47$ [Page 6].

$$
v = \frac{15}{3,600} = 0.004167\text{ m/s}
$$

$$
\text{Re} = \frac{\rho_w v d}{\mu} = \frac{999.1 \times 0.004167 \times 0.95 \times 10^{-3}}{1.139 \times 10^{-3}} = 3.47
$$

**Bước 2 - Tính thành phần tổn thất áp lực do lực ma sát nhớt**: Áp dụng số hạng thứ nhất của phương trình Ergun trên Slide $12$ và Slide $15$ với hệ số $\kappa_V = 228$ và độ rỗng $\epsilon = 0.50$ [Page 6] [Page 7]. Thành phần tổn thất áp lực nhớt qua lớp than antraxit sạch đạt $h_{L,V} = 0.44\text{ m}$ [Page 7].

$$
h_{L,V} = \kappa_V \frac{(1 - \epsilon)^2}{\epsilon^3} \frac{\mu L v}{\rho_w g d^2}
$$

$$
h_{L,V} = 228 \times \frac{(1 - 0.50)^2}{0.50^3} \times \frac{1.139 \times 10^{-3} \times 1.8 \times 0.004167}{999.1 \times 9.81 \times (0.95 \times 10^{-3})^2} = 0.44\text{ m}
$$

**Bước 3 - Tính thành phần tổn thất áp lực do lực quán tính**: Áp dụng số hạng thứ hai của phương trình Ergun trên Slide $12$ và Slide $15$ với hệ số quán tính $\kappa_I = 4.4$ [Page 6] [Page 7]. Thành phần tổn thất áp lực cục bộ do quán tính đạt $h_{L,I} = 0.06\text{ m}$ [Page 7].

$$
h_{L,I} = \kappa_I \frac{1 - \epsilon}{\epsilon^3} \frac{L v^2}{g d}
$$

$$
h_{L,I} = 4.4 \times \frac{1 - 0.50}{0.50^3} \times \frac{1.8 \times 0.004167^2}{9.81 \times 0.95 \times 10^{-3}} = 0.06\text{ m}
$$

**Bước 4 - Tính tổng tổn thất áp lực qua tầng vật liệu lọc sạch**: Cộng hai thành phần tổn thất nhớt và quán tính theo lời giải trên Slide $15$, ta xác định được tổng tổn thất áp lực ban đầu là $h_L = 0.5\text{ m}$ [Page 7]. Nếu sử dụng bể lọc hai lớp vật liệu thì tổng tổn thất áp lực bằng tổng tổn thất của từng lớp cộng lại [Page 7].

$$
h_L = h_{L,V} + h_{L,I} = 0.44 + 0.06 = 0.5\text{ m}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Tổn thất áp lực ban đầu nhỏ hơn nhiều so với cột nước khả dụng của bể lọc nhanh [Page 7] [Page 10].

- **Chuẩn số Reynolds dòng lọc ($\text{Re}$)**: $\text{Re} = 3.47$ (Kiểm tra: $\text{Re} = 3.47\text{ thuộc miền áp dụng phương trình Ergun — Đạt chuẩn Slide } 11\text{–}12$)
- **Tổn thất áp lực thành phần nhớt ($h_{L,V}$)**: $0.44\text{ m}$ (Kiểm tra: $\kappa_V = 228 \in [210, 245]\text{ và }\epsilon = 0.50 \in [0.47, 0.52]\text{ — Đạt chuẩn Slide } 9, 12$)
- **Tổn thất áp lực thành phần quán tính ($h_{L,I}$)**: $0.06\text{ m}$ (Kiểm tra: $\kappa_I = 4.4 \in [3.5, 5.3]\text{ — Đạt chuẩn Slide } 12, 15$)
- **Tổng tổn thất áp lực qua tầng lọc sạch ($h_L$)**: $0.5\text{ m}$ (Kiểm tra: $h_L = 0.5\text{ m} < 1.8\text{–}3.0\text{ m cột nước khả dụng — Đạt chuẩn Slide } 15, 26$)

### Bài tập ch03_5_ex02 (Slide 18–20, Khôi phục theo chuẩn Slide 17): Kiểm Tra Khả Năng Rửa Trôi Hạt Cặn Khi Rửa Ngược Bể Lọc

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy] — Slide $17\text{–}20$): Một bể lọc nhanh được sục rửa ngược ở cường độ $v_{\text{bw}} = 50\text{ m/h}$ tại nhiệt độ nước $T = 15^\circ\text{C}$ [Page 8]. Hãy xác định xem hạt rắn lơ lửng có đường kính $d = 0.1\text{ mm}$ có bị dòng nước rửa ngược cuốn trôi ra khỏi bể lọc hay không [Page 7] [Page 8].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Nhiệt độ nước rửa ngược | $T$ | $15$ | $^\circ\text{C}$ (Slide $18$) |
| Khối lượng riêng của nước ở $15^\circ\text{C}$ | $\rho_w$ | $999.1$ | $\text{kg/m}^3$ (Slide $14, 17$) |
| Độ nhớt động lực học của nước ở $15^\circ\text{C}$ | $\mu$ | $1.139 \times 10^{-3}$ | $\text{Pa}\cdot\text{s}$ (Slide $14, 17$) |
| Vận tốc dòng nước rửa ngược | $v_{\text{bw}}$ | $0.01389$ | $\text{m/s}$ ($50\text{ m/h}$, Slide $18$) |
| Đường kính hạt khảo sát rửa trôi | $d$ | $1.0 \times 10^{-4}$ | $\text{m}$ ($0.1\text{ mm}$, Slide $18$) |
| Khối lượng riêng của hạt rắn khoáng | $\rho_P$ | $2,650$ | $\text{kg/m}^3$ ($2.65\text{ g/mL}$, Slide $9$) |
| Gia tốc trọng trường | $g$ | $9.81$ | $\text{m/s}^2$ (Slide $17$) |

**Bước 1 - Tính chuẩn số Reynolds rửa ngược và hệ số cản thủy lực của hạt**: Đổi vận tốc rửa ngược $v_{\text{bw}} = 50\text{ m/h}$ sang $v_{\text{bw}} = 0.01389\text{ m/s}$ và thay vào công thức Reynolds trên Slide $17$ thu được $\text{Re} = 1.22$ [Page 8]. Vì $\text{Re} = 1.22 < 2$ thuộc chế độ chảy tầng Stokes, hệ số cản thủy lực của hạt đạt $C_d = 19.7$ [Page 8].

$$
v_{\text{bw}} = \frac{50}{3,600} = 0.01389\text{ m/s}, \quad \text{Re} = \frac{\rho_w v_{\text{bw}} d}{\mu} = \frac{999.1 \times 0.01389 \times 0.0001}{1.139 \times 10^{-3}} = 1.22 < 2
$$

$$
C_d = \frac{24}{\text{Re}} = \frac{24}{1.22} = 19.7
$$

**Bước 2 - Tính thể tích hạt cầu và diện tích hình chiếu ngang của hạt**: Áp dụng công thức hình học hạt cầu đường kính $d = 1.0 \times 10^{-4}\text{ m}$ trên Slide $17$, thể tích hạt đạt $V_P = 5.24 \times 10^{-13}\text{ m}^3$ [Page 8]. Diện tích hình chiếu của hạt vuông góc với phương dòng chảy rửa ngược đạt $A_p = 7.85 \times 10^{-9}\text{ m}^2$ [Page 8].

$$
V_P = \frac{\pi d^3}{6} = \frac{\pi \times (0.0001)^3}{6} = 5.24 \times 10^{-13}\text{ m}^3
$$

$$
A_p = \frac{\pi d^2}{4} = \frac{\pi \times (0.0001)^2}{4} = 7.85 \times 10^{-9}\text{ m}^2
$$

**Bước 3 - Tính trọng lượng ngập nước hướng xuống và lực kéo rửa ngược hướng lên**: Hiệu số giữa trọng lực $F_g$ và lực đẩy nổi Archimedes $F_b$ hướng thẳng đứng xuống dưới đạt giá trị $F_g - F_b = 8.48 \times 10^{-9}\text{ N}$ [Page 7] [Page 8]. Lực kéo thủy động của dòng nước rửa ngược hướng thẳng đứng lên trên đạt $F_d = 1.49 \times 10^{-8}\text{ N}$ (tức $14.91 \times 10^{-9}\text{ N}$) [Page 8].

$$
F_g - F_b = (\rho_P - \rho_w) V_P g = (2,650 - 999.1) \times 5.24 \times 10^{-13} \times 9.81 = 8.48 \times 10^{-9}\text{ N}
$$

$$
F_d = C_d \rho_w A_p \frac{v_{\text{bw}}^2}{2} = 19.7 \times 999.1 \times 7.85 \times 10^{-9} \times \frac{0.01389^2}{2} = 1.49 \times 10^{-8}\text{ N}
$$

**Bước 4 - Xác định hợp lực thẳng đứng và đối chiếu phân bố cỡ hạt trong bể lọc**: Thay các thành phần lực vào phương trình cân bằng lực trên Slide $17$, hợp lực hướng xuống đạt $\sum F = -6.43 \times 10^{-9}\text{ N} < 0$ [Page 7] [Page 8]. Do lực kéo hướng lên $F_d$ lớn gấp $1.76\text{ lần}$ trọng lượng ngập nước $F_g - F_b$, hạt mịn $d = 0.1\text{ mm}$ bị cuốn trôi hoàn toàn khỏi bể lọc trong khi hạt cát lọc chuẩn $d = 0.5\text{ mm}$ vẫn được giữ lại trong tầng lọc [Page 8].

$$
\sum F = F_g - F_b - F_d = 8.48 \times 10^{-9} - 14.91 \times 10^{-9} = -6.43 \times 10^{-9}\text{ N} < 0
$$

| Cỡ hạt khảo sát | Đường kính $d$ | Chuẩn số $\text{Re}$ và $C_d$ | Trọng lượng ngập $F_g - F_b$ | Lực kéo rửa ngược $F_d$ | Hợp lực $\sum F$ và Trạng thái hạt |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Hạt cặn mịn đề bài | $0.1\text{ mm}$ ($10^{-4}\text{ m}$) | $\text{Re} = 1.22,\; C_d = 19.7$ | $8.48 \times 10^{-9}\text{ N}$ | $14.91 \times 10^{-9}\text{ N}$ | $-6.43 \times 10^{-9}\text{ N} < 0$ ($\text{Bị rửa trôi}$) |
| Hạt cát lọc chuẩn | $0.5\text{ mm}$ ($5 \times 10^{-4}\text{ m}$) | $\text{Re} = 6.09,\; C_d = 6.26$ | $1.06 \times 10^{-6}\text{ N}$ | $1.18 \times 10^{-7}\text{ N}$ | $+9.42 \times 10^{-7}\text{ N} > 0$ ($\text{Giữ lại trong bể}$) |

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Phép kiểm tra cân bằng lực chứng minh chế độ rửa ngược tách bỏ hiệu quả hạt cặn bẩn $0.1\text{ mm}$ mà không làm trôi hạt cát lọc [Page 7] [Page 8].

- **Chuẩn số Reynolds và hệ số cản hạt ($\text{Re}, C_d$)**: $\text{Re} = 1.22$, $C_d = 19.7$ (Kiểm tra: $\text{Re} = 1.22 < 2\text{ thỏa mãn công thức Stokes } C_d = 24/\text{Re}\text{ — Đạt chuẩn Slide } 17$)
- **Trọng lượng ngập nước hướng xuống ($F_g - F_b$)**: $8.48 \times 10^{-9}\text{ N}$ (Kiểm tra: $V_P = 5.24 \times 10^{-13}\text{ m}^3\text{ tại }\rho_P = 2,650\text{ kg/m}^3\text{ — Đạt chuẩn Slide } 9, 17$)
- **Lực kéo dòng rửa ngược hướng lên ($F_d$)**: $1.49 \times 10^{-8}\text{ N}$ (Kiểm tra: $A_p = 7.85 \times 10^{-9}\text{ m}^2\text{ tại }v_{\text{bw}} = 0.01389\text{ m/s — Đạt chuẩn Slide } 17, 18$)
- **Hợp lực tác dụng lên hạt ($\sum F$)**: $-6.43 \times 10^{-9}\text{ N} < 0$ (Kiểm tra: $F_d > F_g - F_b\text{ nên hạt }0.1\text{ mm bị rửa trôi khỏi bể lọc — Đạt chuẩn Slide } 16\text{–}18$)

### Bài tập ch03_5_ex03 (Slide 23–25, Ảnh chụp lớp học #53, #184, #185): Tính Độ Rỗng Và Chiều Dày Tầng Cát Giãn Nở Khi Rửa Ngược

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy] — Ảnh lớp học #185, #53, #184, Slide $23\text{–}25$): Xác định chiều dày tầng vật liệu giãn nở $L_E$ và tỷ lệ phần trăm giãn nở của bể lọc cát khi sục rửa ngược ở cường độ $v_{\text{bw}} = 40\text{ m/h}$ [Page 9] [Page 10]. Biết chiều dày tầng cát tĩnh ban đầu là $L_F = 0.9\text{ m}$ và nhiệt độ nước rửa ngược là $T = 15^\circ\text{C}$ [Page 9] [Page 10].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Nhiệt độ nước rửa ngược | $T$ | $15$ | $^\circ\text{C}$ (Slide $23$) |
| Khối lượng riêng của nước ở $15^\circ\text{C}$ | $\rho_w$ | $999.1$ | $\text{kg/m}^3$ (Slide $24$, Ảnh #185) |
| Độ nhớt động lực học của nước ở $15^\circ\text{C}$ | $\mu$ | $1.139 \times 10^{-3}$ | $\text{Pa}\cdot\text{s}$ (Slide $24$, Ảnh #185) |
| Vận tốc dòng nước rửa ngược | $v_{\text{bw}}$ | $0.011$ | $\text{m/s}$ ($40\text{ m/h}$, Slide $24$, Ảnh #185) |
| Chiều dày tầng cát lọc tĩnh | $L_F$ | $0.9$ | $\text{m}$ (Slide $23$) |
| Đường kính hạt cát lọc chọn | $d$ | $0.0005$ | $\text{m}$ ($0.5\text{ mm}$, dải $0.4\text{–}0.8\text{ mm}$, Slide $9, 24$) |
| Khối lượng riêng hạt cát lọc chọn | $\rho_P$ | $2,650$ | $\text{kg/m}^3$ ($2.65\text{ kg/L}$, Slide $9, 24$) |
| Hệ số tổn thất nhớt của cát chọn | $\kappa_V$ | $112$ | $\text{Không thứ nguyên}$ (Dải $110\text{–}115$, Slide $12, 24$) |
| Hệ số tổn thất quán tính của cát chọn | $\kappa_I$ | $2.25$ | $\text{Không thứ nguyên}$ (Dải $2.0\text{–}2.5$, Slide $12, 24$) |
| Độ rỗng tầng cát tĩnh chọn | $\epsilon_F$ | $0.42$ | $\text{Không thứ nguyên}$ (Dải $40\text{–}43\%$, Slide $9, 24$) |
| Gia tốc trọng trường | $g$ | $9.81$ | $\text{m/s}^2$ (Slide $22, 25$) |

**Bước 1 - Tính đại lượng phụ trợ không thứ nguyên $X$ của phương trình giãn nở**: Thay các thông số vật liệu cát đã chọn trên Slide $24$ vào biểu thức $X$ trên Slide $22$ và Slide $25$ [Page 9]. Kết quả tính toán cho giá trị đại lượng phụ trợ thứ nhất là $X = 0.1921$ [Page 9].

$$
X = \frac{\mu v_{\text{bw}}}{2 g (\rho_P - \rho_w) d^2}\left(\kappa_V + \frac{\kappa_I \rho_w v_{\text{bw}} d}{\mu}\right)
$$

$$
X = \frac{1.139 \times 10^{-3} \times 0.011}{2 \times 9.81 \times (2,650 - 999.1) \times 0.0005^2}\left(112 + \frac{2.25 \times 999.1 \times 0.011 \times 0.0005}{1.139 \times 10^{-3}}\right) = 0.1921
$$

**Bước 2 - Tính đại lượng phụ trợ không thứ nguyên $Y$ của phương trình giãn nở**: Thay hệ số nhớt $\kappa_V = 112$ và vận tốc rửa ngược $v_{\text{bw}} = 0.011\text{ m/s}$ vào biểu thức $Y$ trên Slide $22$ và Slide $25$ [Page 9]. Giá trị đại lượng phụ trợ thứ hai đạt $Y = 0.1168$ [Page 9].

$$
Y = \frac{\kappa_V \mu v_{\text{bw}}}{3 g (\rho_P - \rho_w) d^2}
$$

$$
Y = \frac{112 \times 1.139 \times 10^{-3} \times 0.011}{3 \times 9.81 \times (2,650 - 999.1) \times 0.0005^2} = 0.1168
$$

**Bước 3 - Tính độ rỗng của tầng cát ở trạng thái giãn nở $\epsilon_E$**: Thay cặp giá trị $X = 0.1921$ và $Y = 0.1168$ vào phương trình căn bậc ba Cardano trên Slide $22$ và Slide $25$ [Page 9]. Độ rỗng của tầng cát trong quá trình rửa ngược tăng từ $\epsilon_F = 0.42$ lên $\epsilon_E = 0.57$ [Page 9].

$$
\epsilon_E = \sqrt[3]{X + \left(X^2 + Y^3\right)^{0.5}} + \sqrt[3]{X - \left(X^2 + Y^3\right)^{0.5}}
$$

$$
\epsilon_E = \sqrt[3]{0.1921 + \left(0.1921^2 + 0.1168^3\right)^{0.5}} + \sqrt[3]{0.1921 - \left(0.1921^2 + 0.1168^3\right)^{0.5}} = 0.57
$$

**Bước 4 - Tính chiều dày tầng cát giãn nở $L_E$ và kiểm tra phần trăm độ giãn nở**: Từ phương trình bảo toàn thể tích hạt rắn trên Slide $21$ và Slide $25$, chiều dày tầng cát khi giãn nở đạt $L_E = 1.21\text{ m}$ [Page 9]. Tỷ lệ phần trăm giãn nở của tầng lọc đạt $E_{\text{bed}} = 34\%$, thỏa mãn hoàn toàn miền thiết kế chuẩn từ $25\%$ đến $37\%$ trên Slide $21$ [Page 9].

$$
L_E = L_F \frac{1 - \epsilon_F}{1 - \epsilon_E} = 0.9 \times \frac{1 - 0.42}{1 - 0.57} = 1.21\text{ m}
$$

$$
E_{\text{bed}} = \left(\frac{L_E}{L_F} - 1\right) \times 100\% = \left(\frac{1.21}{0.9} - 1\right) \times 100\% = 34\%
$$

| Thông số tầng vật liệu lọc cát | Ký hiệu | Trạng thái tầng tĩnh | Trạng thái giãn nở rửa ngược | Đơn vị và Chuẩn kiểm tra Slide |
| :--- | :--- | :--- | :--- | :--- |
| Vận tốc dòng chảy qua tầng cát | $v_F,\; v_{\text{bw}}$ | $5\text{–}15\text{ m/h}$ | $40\text{ m/h}$ ($0.011\text{ m/s}$) | $\text{m/h}$ ($\in [30, 60]\text{ m/h}$, Slide $26$) |
| Hệ số phụ trợ thủy lực Cardano | $X,\; Y$ | $0$ | $X = 0.1921,\; Y = 0.1168$ | $\text{Không thứ nguyên}$ (Slide $25$) |
| Độ rỗng của tầng vật liệu cát | $\epsilon_F,\; \epsilon_E$ | $0.42$ ($42\%$) | $0.57$ ($57\%$) | $\text{Không thứ nguyên}$ (Slide $9, 25$) |
| Chiều dày của tầng vật liệu cát | $L_F,\; L_E$ | $0.90\text{ m}$ | $1.21\text{ m}$ | $\text{m}$ ($\Delta L = 0.31\text{ m}$, Slide $25$) |
| Tỷ lệ phần trăm giãn nở tầng lọc | $E_{\text{bed}}$ | $0\%$ | $34\%$ ($0.34$) | $\%$ ($\in [25\%, 37\%]$, Slide $21, 25$) |

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Độ giãn nở $34\%$ đảm bảo rửa sạch cặn bám trong khe rỗng mà không làm trôi hạt cát lọc qua máng thu nước [Page 9] [Page 10].

- **Hai đại lượng không thứ nguyên ($X, Y$)**: $X = 0.1921$, $Y = 0.1168$ (Kiểm tra: $\kappa_V = 112 \in [110, 115],\;\kappa_I = 2.25 \in [2.0, 2.5]\text{ — Đạt chuẩn Slide } 12, 24\text{–}25$)
- **Độ rỗng tầng cát giãn nở ($\epsilon_E$)**: $\epsilon_E = 0.57$ (Kiểm tra: $\epsilon_E = 0.57 > \epsilon_F = 0.42\text{ — Đạt chuẩn Slide } 25$)
- **Chiều dày tầng cát giãn nở ($L_E$)**: $1.21\text{ m}$ (Kiểm tra: $L_E = 1.21\text{ m} > L_F = 0.90\text{ m — Đạt chuẩn Slide } 25$)
- **Độ giãn nở tầng vật liệu lọc ($E_{\text{bed}}$)**: $34\%$ (Kiểm tra: $25\% \le 34\% \le 37\%\text{ — Đạt chuẩn Slide } 21, 25$)

### Bài tập ch03_5_ex04 (Slide 27–31, Ảnh chụp lớp học #54–#56, #184): Thiết Kế Hệ Thống Bể Lọc Nhanh Hai Lớp Vật Liệu Cát Và Than Antraxit

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy] trên Slide $28, 29, 31$ tại Ảnh #54, #55, #56 kết hợp [Lời giải khôi phục theo chuẩn slide của thầy] trên Slide $30$ và bảng phấn Ảnh #184): Thiết kế hệ thống bể lọc nhanh hai lớp vật liệu (gồm lớp cát thạch anh và lớp than antraxit) cho nhà máy xử lý nước thải có công suất thiết kế $Q = 230,000\text{ m}^3\text{/ngày}$ [Page 10] [Page 11]. Nội dung thiết kế bao gồm xác định tổng diện tích lọc, số lượng ô bể lọc, kích thước hình học mỗi bể, chiều cao đặt máng thu nước rửa ngược và kiểm tra tỷ lệ thu hồi nước sạch sau lọc [Page 10] [Page 11].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Công suất thiết kế trạm xử lý | $Q$ | $230,000$ | $\text{m}^3\text{/ngày}$ (Slide $27$) |
| Vận tốc lọc thiết kế chọn | $v_F$ | $15$ | $\text{m}^3/(\text{m}^2\cdot\text{h})$ (Dải $5\text{–}15$, Slide $26, 28$) |
| Chiều cao lớp nước trên mặt lọc chọn | $H_{\text{water}}$ | $2.0$ | $\text{m}$ (Dải $1.8\text{–}3.0\text{ m}$, Slide $26, 28$) |
| Tổng chiều dày vật liệu lọc tĩnh | $L_F$ | $0.9$ ($0.3 + 0.6$) | $\text{m}$ ($0.3\text{ m}$ cát $+ 0.6\text{ m}$ than, Slide $5, 28$) |
| Chiều dày hệ thống sàn thu nước đáy | $H_{\text{ud}}$ | $0.5$ | $\text{m}$ (Dải $0.3\text{–}0.6\text{ m}$, Slide $26, 28$) |
| Chiều cao bảo vệ thành bể chọn | $H_{\text{fb}}$ | $0.6$ | $\text{m}$ (Slide $29$, Ảnh #55) |
| Cường độ nước rửa ngược chọn | $v_{\text{bw}}$ | $40$ | $\text{m}^3/(\text{m}^2\cdot\text{h})$ (Dải $30\text{–}60$, Slide $26, 28$) |
| Thời gian một chu kỳ lọc chọn | $t_F$ | $48$ ($2$) | $\text{h}$ ($2\text{ ngày}$, dải $1\text{–}4\text{ ngày}$, Slide $26, 31$) |
| Thời gian một lần rửa ngược chọn | $t_{\text{bw}}$ | $0.25$ ($15$) | $\text{h}$ ($15\text{ phút}$, dải $10\text{–}20\text{ phút}$, Slide $26, 31$) |
| Thời gian lọc xả bỏ đầu chu kỳ chọn | $t_{\text{FTW}}$ | $1.0$ ($60$) | $\text{h}$ ($60\text{ phút}$, dải $15\text{ phút–}2\text{ h}$, Slide $26, 31$) |

**Bước 1 - Tính tổng diện tích bề mặt lọc và chọn số lượng ô bể lọc**: Từ công suất $Q = 230,000\text{ m}^3\text{/ngày}$ và vận tốc lọc $v_F = 15\text{ m}^3/(\text{m}^2\cdot\text{h})$, tổng diện tích lọc yêu cầu trên Slide $29$ đạt $A = 640\text{ m}^2$ (trên slide hiển thị nhầm tử số $200,000$ nhưng kết quả $640\text{ m}^2$ tính đúng từ $230,000 / 360 = 638.9\text{ m}^2$) [Page 10] [Page 11]. Để diện tích mỗi ô bể lọc không vượt quá $100\text{ m}^2$, giảng viên chọn tổng cộng $N = 9\text{ bể lọc}$ (gồm $8\text{ bể}$ vận hành đồng thời và $1\text{ bể}$ dự phòng rửa ngược), suy ra diện tích mỗi ô bể là $A_{\text{each}} = 80\text{ m}^2$ với kích thước $L \times W = 10\text{ m} \times 8\text{ m}$ [Page 10].

$$
A = \frac{Q}{v_F \times 24} = \frac{230,000}{15 \times 24} = 638.9\text{ m}^2 \approx 640\text{ m}^2
$$

$$
A_{\text{each}} = \frac{A}{N_{\text{active}}} = \frac{640}{8} = 80\text{ m}^2 \le 100\text{ m}^2 \implies L \times W = 10\text{ m} \times 8\text{ m}
$$

**Bước 2 - Tính tổng chiều sâu xây dựng của mỗi ô bể lọc**: Cộng bốn thành phần chiều cao theo phương thẳng đứng trên Slide $29$ gồm lớp vật liệu lọc $0.9\text{ m}$, lớp nước khả dụng $2.0\text{ m}$, sàn thu nước đáy $0.5\text{ m}$ và chiều cao bảo vệ $0.6\text{ m}$ [Page 10]. Tổng chiều sâu xây dựng của mỗi ô bể lọc đạt $D = 4.0\text{ m}$, thỏa mãn khoảng chuẩn từ $4\text{ m}$ đến $8\text{ m}$ trên Slide $26$ [Page 10].

$$
D = L_F + H_{\text{water}} + H_{\text{ud}} + H_{\text{fb}} = 0.9 + 2.0 + 0.5 + 0.6 = 4.0\text{ m}
$$

**Bước 3 - Tính chiều dày tầng lọc hai lớp giãn nở và chiều cao đặt máng thu nước rửa lọc**: Khi sục rửa ngược ở cường độ $v_{\text{bw}} = 40\text{ m}^3/(\text{m}^2\cdot\text{h})$ theo Slide $30$ và sơ đồ bảng phấn Ảnh #184, tổng chiều dày tầng lọc giãn nở đạt $L_E = 1.20\text{ m}$ (hoặc $L_E = 0.40 + 0.84 = 1.24\text{ m}$ khi tính riêng lớp cát $\epsilon_E = 0.57$ và lớp than antraxit $\epsilon_E = 0.64$) [Page 9] [Page 10]. Cộng thêm khoảng lưu không an toàn $0.3\text{ m}$ theo bảng chuẩn Slide $26$, chiều cao đặt mép máng thu nước rửa lọc tính từ mặt sàn đỡ vật liệu đạt $H_{\text{trough}} = 1.5\text{ m}$ (hoặc $1.6\text{ m}$) [Page 10].

$$
L_E = L_{E,\text{sand}} + L_{E,\text{anth}} = 0.3 \times \frac{1 - 0.42}{1 - 0.57} + 0.6 \times \frac{1 - 0.50}{1 - 0.64} = 0.40 + 0.84 = 1.24\text{ m}\; (\approx 1.20\text{ m})
$$

$$
H_{\text{trough}} = L_E + \Delta H_{\text{clearance}} = 1.20 + 0.30 = 1.50\text{ m}\; (\text{hoặc } 1.24 + 0.36 = 1.60\text{ m})
$$

**Bước 4 - Tính sản lượng nước lọc và kiểm tra tỷ lệ thu hồi nước sạch sau lọc**: Theo lời giải trên Slide $31$ (Ảnh #56), tổng thể tích nước lọc trên mỗi đơn vị diện tích trong một chu kỳ $t_F = 48\text{ h}$ là $720\text{ m}^3/\text{m}^2$, lượng nước dùng cho rửa ngược là $10\text{ m}^3/\text{m}^2$ và lượng nước xả bỏ đầu chu kỳ là $15\text{ m}^3/\text{m}^2$ [Page 10]. Tỷ lệ thu hồi nước sạch của hệ thống đạt $R_{\text{rec}} = 96.5\% > 95\%$, thỏa mãn tiêu chuẩn thiết kế trên Slide $26$ [Page 10].

$$
R_{\text{rec}} = \frac{v_F t_F - v_{\text{bw}} t_{\text{bw}} - v_F t_{\text{FTW}}}{v_F t_F}
$$

$$
R_{\text{rec}} = \frac{(15 \times 48) - (40 \times 0.25) - (15 \times 1.0)}{15 \times 48} = \frac{720 - 10 - 15}{720} = \frac{695}{720} = 96.5\%
$$

| Hạng mục thiết kế bể lọc hai lớp | Ký hiệu | Giá trị tính toán | Giới hạn chuẩn Slide 26 | Đánh giá thiết kế |
| :--- | :--- | :--- | :--- | :--- |
| Diện tích mỗi ô bể lọc ($9\text{ ô} = 8 + 1$) | $A_{\text{each}}$ | $80\text{ m}^2$ ($10\text{ m} \times 8\text{ m}$) | $\le 100\text{ m}^2$ | $\text{Đạt chuẩn Slide } 26, 29$ |
| Lớp cát thạch anh dưới đáy | $L_{\text{sand}},\; L_{E,\text{sand}}$ | $L_F = 0.30\text{ m},\; L_E = 0.40\text{ m}$ | $0.25\text{–}0.30\text{ m}$ (Slide $5$) | $\text{Giãn nở } 34\% \in [25\%, 37\%]$ |
| Lớp than antraxit phía trên | $L_{\text{anth}},\; L_{E,\text{anth}}$ | $L_F = 0.60\text{ m},\; L_E = 0.84\text{ m}$ | $0.45\text{–}0.60\text{ m}$ (Slide $5$) | $\text{Giãn nở } 39\%,\text{ tổng } L_E = 1.24\text{ m}$ |
| Chiều cao mép máng thu nước rửa | $H_{\text{trough}}$ | $1.50\text{–}1.60\text{ m}$ | $L_E + (0.3\text{–}0.5\text{ m})$ | $\text{Đạt chuẩn Slide } 26, 30$ |
| Tổng chiều sâu xây dựng bể lọc | $D$ | $4.0\text{ m}$ | $4.0\text{–}8.0\text{ m}$ | $\text{Đạt chuẩn Slide } 26, 29$ |
| Tỷ lệ thu hồi nước sạch sau lọc | $R_{\text{rec}}$ | $96.5\%$ ($695 / 720\text{ m}^3/\text{m}^2$) | $> 95\%$ | $\text{Đạt chuẩn Slide } 26, 31$ |

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng. Hệ thống $9\text{ ô bể lọc}$ đảm bảo vận hành liên tục ở công suất $230,000\text{ m}^3\text{/ngày}$ ngay cả khi có $1\text{ ô}$ ngưng lọc để rửa ngược [Page 10] [Page 11].

- **Tổng diện tích lọc và số ô bể ($A, N$)**: $A = 640\text{ m}^2$, chọn $N = 9\text{ bể}$ ($8\text{ bể}$ lọc $+ 1\text{ bể}$ rửa ngược) (Kiểm tra: $A_{\text{each}} = 80\text{ m}^2 \le 100\text{ m}^2\text{ — Đạt chuẩn Slide } 26, 29$)
- **Kích thước hình học mỗi ô bể lọc ($L \times W \times D$)**: $10\text{ m} \times 8\text{ m} \times 4\text{ m}$ (Kiểm tra: $D = 4.0\text{ m} \in [4.0, 8.0]\text{ m và }L_F = 0.9\text{ m} \in [0.6, 1.8]\text{ m — Đạt chuẩn Slide } 26, 29$)
- **Chiều dày tầng lọc giãn nở và cao trình máng rửa ($L_E, H_{\text{trough}}$)**: $L_E = 1.20\text{–}1.24\text{ m}$, $H_{\text{trough}} = 1.50\text{–}1.60\text{ m}$ (Kiểm tra: $H_{\text{trough}} = L_E + 0.3\text{ m} \in [L_E + 0.3\text{ m}, L_E + 0.5\text{ m}]\text{ — Đạt chuẩn Slide } 26, 30$)
- **Tỷ lệ thu hồi nước sạch sau lọc ($R_{\text{rec}}$)**: $96.5\%$ (Kiểm tra: $R_{\text{rec}} = 96.5\% > 95\%\text{ — Đạt chuẩn Slide } 26, 31$)
