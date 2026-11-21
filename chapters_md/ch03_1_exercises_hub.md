### Bài tập ch03_1_ex01 (Slide 30–32): Thiết kế mương dẫn và tính tổn thất cột nước qua song chắn rác thẳng đứng

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy] — Ảnh lớp học #19, #20, Slide 30–32): Thiết kế mương dẫn đặt song chắn rác cho lưu lượng giờ cao điểm $Q = 1,000\text{ m}^3/\text{h}$ ($0.278\text{ m}^3/\text{s}$) với độ dốc đáy mương $S = 0.0001\text{ m/m}$ và chiều cao bảo vệ $h_{\text{bv}} = 0.5\text{ m}$ [Page 15]. Tính tổn thất cột nước qua song chắn rác khi sạch và khi bị tắc nghẽn $50\%$ diện tích khe hở với bề rộng thanh chắn $b = 10\text{ mm}$ ($0.01\text{ m}$) và khe hở thông thủy $e = 40\text{ mm}$ ($0.04\text{ m}$) [Page 15].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng thiết kế giờ cao điểm | $Q$ | $1,000$ ($0.278$) | $\text{m}^3/\text{h}$ ($\text{m}^3/\text{s}$, Slide 30) |
| Độ dốc thủy lực đáy mương | $S$ | $0.0001$ | $\text{m/m}$ (Slide 30) |
| Hệ số nhám bê tông trát nhẵn | $n$ | $0.012$ | $-$ (Slide 26) |
| Bề rộng mương chọn trước | $W$ | $1.5$ | $\text{m}$ (Slide 31) |
| Chiều cao bảo vệ mương dẫn | $h_{\text{bv}}$ | $0.5$ | $\text{m}$ (Slide 30) |
| Bề rộng một thanh chắn | $b$ | $10$ ($0.01$) | $\text{mm}$ ($\text{m}$, Slide 30) |
| Khe hở thông thủy giữa các thanh | $e$ | $40$ ($0.04$) | $\text{mm}$ ($\text{m}$, Slide 30) |
| Hệ số lưu lượng khi song chắn sạch | $C_{\text{clean}}$ | $0.7$ | $-$ (Slide 28) |
| Hệ số lưu lượng khi tắc nghẽn $50\%$ | $C_{\text{clog}}$ | $0.6$ | $-$ (Slide 28) |

**Bước 1 - Xác định chiều sâu mực nước và vận tốc tiếp cận trong mương dẫn**: Áp dụng đồng thời phương trình liên tục và phương trình Manning với bề rộng mương chọn trước $W = 1.5\text{ m}$ và độ nhám $n = 0.012$ [Page 13] [Page 15]. Giải hệ phương trình thu được chiều sâu dòng chảy $D = 0.5\text{ m}$, vận tốc tiếp cận $v_{\text{app}} = 0.37\text{ m/s}$ và tổng chiều cao mương $H = 1.0\text{ m}$.

$$
v = \frac{Q}{W \times D} = \frac{\frac{1,000}{3,600}}{1.5 \times D}
$$

$$
v = \frac{1}{n} R^{2/3} S^{1/2} = \frac{1}{0.012} \left(\frac{1.5 D}{1.5 + 2D}\right)^{2/3} (0.0001)^{1/2}
$$

$$
\Rightarrow D = 0.5\text{ m}, \quad v_{\text{app}} = 0.37\text{ m/s}, \quad H = 0.5 + 0.5 = 1.0\text{ m}
$$

**Bước 2 - Tính số thanh đan, số khe hở và diện tích khe hở ngập nước**: Từ quan hệ hình học trên mặt cắt ngang mương rộng $W = 1,500\text{ mm}$, tính được số thanh chắn $N_{\text{bars}} = 29\text{ thanh}$ và số khe hở thông thủy $N_{\text{spaces}} = 30\text{ khe}$ [Page 14]. Tổng diện tích khe hở ngập nước của song chắn đặt thẳng đứng đạt $A_{\text{space}} = 0.6\text{ m}^2$ và vận tốc dòng chảy qua khe lúc sạch đạt $v_{\text{thru}} = 0.46\text{ m/s}$.

$$
N_{\text{bars}} = \frac{W - e}{b + e} = \frac{1,500 - 40}{10 + 40} = 29.2 \Rightarrow 29\text{ thanh}, \quad N_{\text{spaces}} = 29 + 1 = 30\text{ khe}
$$

$$
A_{\text{space}} = N_{\text{spaces}} \times e \times D = 30 \times 0.04 \times 0.5 = 0.6\text{ m}^2
$$

$$
v_{\text{thru}} = \frac{Q}{A_{\text{space}}} = \frac{\frac{1,000}{3,600}}{0.6} = 0.46\text{ m/s}
$$

**Bước 3 - Tính tổn thất cột nước qua song chắn rác khi sạch và khi bị tắc nghẽn $50\%$**: Thay vận tốc qua khe $v_{\text{thru}} = 0.46\text{ m/s}$ và vận tốc tiếp cận $v_{\text{app}} = 0.37\text{ m/s}$ vào phương trình lỗ chảy với $C_{\text{clean}} = 0.7$, thu được tổn thất cột nước khi sạch là $h_{L,\text{clean}} = 5.4\text{ mm}$ [Page 14]. Khi song chắn bị tắc nghẽn $50\%$ diện tích khe hở ($v_{\text{clog}} = 0.92\text{ m/s}$ và $C_{\text{clog}} = 0.6$), tổn thất cột nước tăng lên $h_{L,\text{clog}} = 60\text{ mm}$.

$$
h_{L,\text{clean}} = \frac{1}{C_{\text{clean}}}\left(\frac{v_{\text{thru}}^2 - v_{\text{app}}^2}{2g}\right) = \frac{1}{0.7}\left(\frac{0.46^2 - 0.37^2}{2 \times 9.81}\right) = 0.00544\text{ m} = 5.4\text{ mm}
$$

$$
h_{L,\text{clog}} = \frac{1}{C_{\text{clog}}}\left(\frac{v_{\text{clog}}^2 - v_{\text{app}}^2}{2g}\right) = \frac{1}{0.6}\left(\frac{0.92^2 - 0.37^2}{2 \times 9.81}\right) = 0.06\text{ m} = 60\text{ mm}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Kích thước mương dẫn ($W, D, H$)**: $W = 1.5\text{ m}$, $D = 0.5\text{ m}$, $H = 1.0\text{ m}$ (Kiểm tra: $h_{\text{bv}} = 0.5\text{ m}$ — Đạt chuẩn Slide 30–31)
- **Vận tốc dòng chảy tiếp cận ($v_{\text{app}}$)**: $0.37\text{ m/s}$ (Kiểm tra: $0.3 \le 0.37 \le 0.6\text{ m/s}$ — Đạt chuẩn Slide 29)
- **Số thanh, số khe và diện tích khe ($N_{\text{bars}}$, $N_{\text{spaces}}$, $A_{\text{space}}$)**: $29\text{ thanh}$, $30\text{ khe}$, $0.6\text{ m}^2$ (Kiểm tra: $v_{\text{thru}} = 0.46\text{ m/s}$ — Đạt chuẩn Slide 32)
- **Tổn thất cột nước sạch và tắc $50\%$ ($h_{L,\text{clean}}$, $h_{L,\text{clog}}$)**: $5.4\text{ mm}$ và $60\text{ mm}$ (Kiểm tra: $60\text{ mm} < 150\text{ mm}$ — Đạt chuẩn Slide 29)

### Bài tập ch03_1_ex02 (Slide 33–37): Tính tổn thất cột nước qua song chắn rác đặt nghiêng góc 50°, 55° và 60°

**Đề bài** ([Lời giải từ ảnh chụp slide của thầy] cho góc $50^\circ$ tại Ảnh #139 Slide 34 kết hợp [Lời giải khôi phục theo chuẩn slide của thầy] cho góc $55^\circ, 60^\circ$): Từ kết quả thiết kế mương dẫn của bài tập `ch03_1_ex01` ($Q = 1,000\text{ m}^3/\text{h}$, $W = 1.5\text{ m}$, $D = 0.5\text{ m}$, $N_{\text{spaces}} = 30\text{ khe}$, $e = 0.04\text{ m}$), hãy xác định lại vận tốc qua khe và tổn thất cột nước qua song chắn rác sạch khi đặt nghiêng góc $\theta = 50^\circ$, $\theta = 55^\circ$ và $\theta = 60^\circ$ so với phương ngang [Page 16]. Nhận xét ảnh hưởng của góc nghiêng $\theta$ đến vận tốc dòng chảy qua khe và tổn thất cột nước [Page 16].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng giờ cao điểm | $Q$ | $1,000$ ($0.278$) | $\text{m}^3/\text{h}$ ($\text{m}^3/\text{s}$, Slide 30) |
| Bề rộng và chiều sâu nước trong mương | $W, D$ | $1.5$ và $0.5$ | $\text{m}$ (Slide 31) |
| Số khe hở và bề rộng một khe | $N_{\text{spaces}}$, $e$ | $30$ và $0.04$ | $\text{khe}$ và $\text{m}$ (Slide 32) |
| Các góc nghiêng khảo sát từ phương ngang | $\theta$ | $50^\circ, 55^\circ, 60^\circ$ | $\text{Độ}$ (Slide 33) |
| Hệ số lưu lượng qua song chắn sạch | $C_{\text{clean}}$ | $0.7$ | $-$ (Slide 28) |
| Gia tốc trọng trường trên Slide 34 | $g$ | $9.8$ | $\text{m/s}^2$ (Slide 34) |

**Bước 1 - Tính diện tích ngập nước, vận tốc và tổn thất cột nước tại góc nghiêng $\theta = 50^\circ$**: Khi đặt nghiêng góc $\theta = 50^\circ$ so với phương ngang, chiều dài ngập nước của thanh chắn tăng theo tỷ số $SL = \frac{D}{\sin 50^\circ}$ nên diện tích khe hở đạt $A_{\text{space}} = 0.78\text{ m}^2$ và diện tích mặt nghiêng đạt $A_{\text{total}} = 0.98\text{ m}^2$ [Page 16]. Từ đó tính được vận tốc qua khe $v_{\text{thru}} = 0.35\text{ m/s}$, vận tốc tới gần $v_{\text{app}} = 0.28\text{ m/s}$ và tổn thất cột nước $h_L(50^\circ) = 3.2\text{ mm}$.

$$
A_{\text{space}}(50^\circ) = \frac{N_{\text{spaces}} \times e \times D}{\sin 50^\circ} = \frac{30 \times 0.04 \times 0.5}{\sin 50^\circ} = 0.78\text{ m}^2, \quad A_{\text{total}}(50^\circ) = \frac{1.5 \times 0.5}{\sin 50^\circ} = 0.98\text{ m}^2
$$

$$
v_{\text{thru}}(50^\circ) = \frac{\frac{1,000}{3,600}}{0.78} = 0.35\text{ m/s}, \quad v_{\text{app}}(50^\circ) = \frac{\frac{1,000}{3,600}}{0.98} = 0.28\text{ m/s}
$$

$$
h_L(50^\circ) = \frac{1}{0.7} \times \frac{0.35^2 - 0.28^2}{2 \times 9.8} = 0.0032\text{ m} = 3.2\text{ mm}
$$

**Bước 2 - Tính diện tích ngập nước, vận tốc và tổn thất cột nước tại góc nghiêng $\theta = 55^\circ$**: Áp dụng công thức hình học mặt nghiêng tại góc $\theta = 55^\circ$, thu được diện tích khe hở ngập nước $A_{\text{space}} = 0.73\text{ m}^2$ và diện tích mặt nghiêng $A_{\text{total}} = 0.92\text{ m}^2$ [Page 16]. Vận tốc qua khe đạt $v_{\text{thru}} = 0.38\text{ m/s}$, vận tốc tới gần đạt $v_{\text{app}} = 0.30\text{ m/s}$ và tổn thất cột nước đạt $h_L(55^\circ) = 4.0\text{ mm}$.

$$
A_{\text{space}}(55^\circ) = \frac{30 \times 0.04 \times 0.5}{\sin 55^\circ} = 0.73\text{ m}^2, \quad A_{\text{total}}(55^\circ) = \frac{1.5 \times 0.5}{\sin 55^\circ} = 0.92\text{ m}^2
$$

$$
v_{\text{thru}}(55^\circ) = \frac{\frac{1,000}{3,600}}{0.73} = 0.38\text{ m/s}, \quad v_{\text{app}}(55^\circ) = \frac{\frac{1,000}{3,600}}{0.92} = 0.30\text{ m/s}
$$

$$
h_L(55^\circ) = \frac{1}{0.7} \times \frac{0.38^2 - 0.30^2}{2 \times 9.8} = 0.0040\text{ m} = 4.0\text{ mm}
$$

**Bước 3 - Tính diện tích ngập nước, vận tốc và tổn thất cột nước tại góc nghiêng $\theta = 60^\circ$**: Tại góc nghiêng $\theta = 60^\circ$ so với phương ngang, diện tích khe hở ngập nước bằng $A_{\text{space}} = 0.69\text{ m}^2$ và tổng diện tích mặt nghiêng bằng $A_{\text{total}} = 0.87\text{ m}^2$ [Page 16]. Vận tốc dòng chảy qua khe bằng $v_{\text{thru}} = 0.40\text{ m/s}$, vận tốc tới gần bằng $v_{\text{app}} = 0.32\text{ m/s}$ và tổn thất cột nước bằng $h_L(60^\circ) = 4.2\text{ mm}$.

$$
A_{\text{space}}(60^\circ) = \frac{30 \times 0.04 \times 0.5}{\sin 60^\circ} = 0.69\text{ m}^2, \quad A_{\text{total}}(60^\circ) = \frac{1.5 \times 0.5}{\sin 60^\circ} = 0.87\text{ m}^2
$$

$$
v_{\text{thru}}(60^\circ) = \frac{\frac{1,000}{3,600}}{0.69} = 0.40\text{ m/s}, \quad v_{\text{app}}(60^\circ) = \frac{\frac{1,000}{3,600}}{0.87} = 0.32\text{ m/s}
$$

$$
h_L(60^\circ) = \frac{1}{0.7} \times \frac{0.40^2 - 0.32^2}{2 \times 9.8} = 0.0042\text{ m} = 4.2\text{ mm}
$$

**Bước 4 - Bảng đối chiếu tổng hợp và nhận xét ảnh hưởng của góc nghiêng $\theta$**: Khi giảm góc nghiêng $\theta$ so với phương ngang từ $90^\circ$ xuống $50^\circ$, chiều dài ngập nước $SL = \frac{D}{\sin\theta}$ tăng lên làm mở rộng diện tích khe hở $A_{\text{space}}$, nhờ đó làm giảm vận tốc qua khe $v_{\text{thru}}$ và giảm tổn thất cột nước $h_L$ qua song chắn rác.

| Góc nghiêng $\theta$ | Diện tích khe $A_{\text{space}}$ | Vận tốc qua khe $v_{\text{thru}}$ | Vận tốc tới gần $v_{\text{approach}}$ | Tổn thất cột nước $h_L$ |
| :--- | :--- | :--- | :--- | :--- |
| $90^\circ$ (Thẳng đứng) | $0.60\text{ m}^2$ | $0.46\text{ m/s}$ | $0.37\text{ m/s}$ | $5.4\text{ mm}$ |
| $60^\circ$ (Nghiêng) | $0.69\text{ m}^2$ | $0.40\text{ m/s}$ | $0.32\text{ m/s}$ | $4.2\text{ mm}$ |
| $55^\circ$ (Nghiêng) | $0.73\text{ m}^2$ | $0.38\text{ m/s}$ | $0.30\text{ m/s}$ | $4.0\text{ mm}$ |
| $50^\circ$ (Nghiêng) | $0.78\text{ m}^2$ | $0.35\text{ m/s}$ | $0.28\text{ m/s}$ | $3.2\text{ mm}$ |

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Phương án góc nghiêng $\theta = 50^\circ$ ($h_L(50^\circ)$)**: $3.2\text{ mm}$ với $v_{\text{thru}} = 0.35\text{ m/s}$ (Kiểm tra: $3.2\text{ mm} < 150\text{ mm}$ — Đạt chuẩn Slide 29 & 34)
- **Phương án góc nghiêng $\theta = 55^\circ$ ($h_L(55^\circ)$)**: $4.0\text{ mm}$ với $v_{\text{thru}} = 0.38\text{ m/s}$ (Kiểm tra: $4.0\text{ mm} < 150\text{ mm}$ — Đạt chuẩn Slide 29)
- **Phương án góc nghiêng $\theta = 60^\circ$ ($h_L(60^\circ)$)**: $4.2\text{ mm}$ với $v_{\text{thru}} = 0.40\text{ m/s}$ (Kiểm tra: $4.2\text{ mm} < 150\text{ mm}$ — Đạt chuẩn Slide 29)
- **Quy luật thủy lực khi giảm góc nghiêng ($\theta$)**: $h_L(50^\circ) < h_L(55^\circ)$ và $h_L(55^\circ) < h_L(60^\circ)$ (Kiểm tra: giảm $\theta$ giúp giảm $v_{\text{thru}}$ và $h_L$ — Đạt yêu cầu)

### Bài tập proj_ch03_1_hw01 (Slide 35/38 - Homework): Thiết kế mương dẫn đặt song chắn rác thô cào cơ giới nghiêng 75°

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy] — Ảnh đề bài lớp học #21, #140, #141, Slide 35/38): Xác định kích thước mương dẫn cho song chắn rác thô cào cơ giới phục vụ lưu lượng thiết kế $Q = 40,000\text{ m}^3/\text{d}$ ($0.463\text{ m}^3/\text{s}$) [Page 14] [Page 15]. Song chắn rác đặt nghiêng góc $\theta = 75^\circ$ so với phương ngang, sử dụng các thanh chắn có bề rộng $b = 12\text{ mm}$ ($0.012\text{ m}$), khoảng cách khe hở thông thủy $e = 12\text{ mm}$ ($0.012\text{ m}$) và vận tốc dòng chảy thượng lưu phải lớn hơn $0.4\text{ m/s}$. Tính tổn thất cột nước qua song chắn rác khi sạch và khi bị tắc nghẽn $50\%$.

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng thiết kế | $Q$ | $40,000$ ($0.463$) | $\text{m}^3/\text{d}$ ($\text{m}^3/\text{s}$, Slide 35) |
| Góc nghiêng từ phương ngang | $\theta$ | $75^\circ$ | $\text{Độ}$ ($15^\circ$ so với phương đứng, Slide 29) |
| Bề rộng thanh và khe hở | $b, e$ | $12$ và $12$ | $\text{mm}$ ($0.012\text{ m}$, Slide 35) |
| Bề rộng mương và độ dốc đáy chọn | $W, S$ | $1.5$ và $0.0001$ | $\text{m}$ và $\text{m/m}$ (Slide 31) |
| Hệ số nhám bê tông và chiều cao bảo vệ | $n, h_{\text{bv}}$ | $0.012$ và $0.5$ | $-$ và $\text{m}$ (Slide 26, 30) |
| Hệ số lưu lượng sạch và tắc $50\%$ | $C_{\text{clean}}$, $C_{\text{clog}}$ | $0.7$ và $0.6$ | $-$ (Slide 28) |

**Bước 1 - Tính chiều sâu mực nước và vận tốc dòng chảy trong mương thượng lưu**: Giải đồng thời phương trình liên tục và phương trình Manning với bề rộng mương $W = 1.5\text{ m}$, độ dốc đáy $S = 0.0001\text{ m/m}$ và hệ số nhám $n = 0.012$ [Page 13]. Thu được chiều sâu mực nước $D = 0.72\text{ m}$, vận tốc dòng chảy thượng lưu $v = 0.43\text{ m/s}$ và tổng chiều cao mương $H = 1.22\text{ m}$.

$$
v = \frac{Q}{W \times D} = \frac{0.463}{1.5 \times D}
$$

$$
v = \frac{1}{0.012}\left(\frac{1.5 D}{1.5 + 2D}\right)^{2/3}(0.0001)^{1/2} \Rightarrow D = 0.72\text{ m}, \quad v = 0.43\text{ m/s}
$$

$$
H = D + h_{\text{bv}} = 0.72 + 0.50 = 1.22\text{ m}
$$

**Bước 2 - Tính số thanh chắn, diện tích mặt nghiêng và vận tốc qua khe**: Với bề rộng mương $W = 1,500\text{ mm}$, số thanh chắn tính được vừa tròn $N_{\text{bars}} = 62\text{ thanh}$ và số khe hở là $N_{\text{spaces}} = 63\text{ khe}$ [Page 14]. Tại góc nghiêng $\theta = 75^\circ$, diện tích khe hở ngập nước đạt $A_{\text{space}} = 0.56\text{ m}^2$, tổng diện tích mặt nghiêng đạt $A_{\text{total}} = 1.12\text{ m}^2$, vận tốc qua khe đạt $v_{\text{thru}} = 0.83\text{ m/s}$ và vận tốc tới gần đạt $v_{\text{app}} = 0.41\text{ m/s}$.

$$
N_{\text{bars}} = \frac{W - e}{b + e} = \frac{1,500 - 12}{12 + 12} = 62\text{ thanh}, \quad N_{\text{spaces}} = 62 + 1 = 63\text{ khe}
$$

$$
A_{\text{space}} = \frac{N_{\text{spaces}} \times e \times D}{\sin 75^\circ} = \frac{63 \times 0.012 \times 0.72}{\sin 75^\circ} = 0.56\text{ m}^2, \quad A_{\text{total}} = \frac{1.5 \times 0.72}{\sin 75^\circ} = 1.12\text{ m}^2
$$

$$
v_{\text{thru}} = \frac{0.463}{0.56} = 0.83\text{ m/s}, \quad v_{\text{app}} = \frac{0.463}{1.12} = 0.41\text{ m/s}
$$

**Bước 3 - Tính tổn thất cột nước qua song chắn cơ giới khi sạch và khi tắc nghẽn $50\%$**: Áp dụng phương trình lỗ chảy, tổn thất cột nước qua song chắn sạch ($C_{\text{clean}} = 0.7$) bằng $h_{L,\text{clean}} = 38\text{ mm}$ [Page 14]. Khi bị tắc nghẽn $50\%$ diện tích khe hở ($v_{\text{clog}} = 1.66\text{ m/s}$ và $C_{\text{clog}} = 0.6$), tổn thất cột nước bằng $h_{L,\text{clog}} = 220\text{ mm}$.

$$
h_{L,\text{clean}} = \frac{1}{0.7}\left(\frac{0.83^2 - 0.41^2}{2 \times 9.81}\right) = 0.038\text{ m} = 38\text{ mm}
$$

$$
h_{L,\text{clog}} = \frac{1}{0.6}\left(\frac{1.66^2 - 0.41^2}{2 \times 9.81}\right) = 0.22\text{ m} = 220\text{ mm}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Kích thước mương dẫn ($W, D, H$)**: $W = 1.5\text{ m}$, $D = 0.72\text{ m}$, $H = 1.22\text{ m}$ (Kiểm tra: $h_{\text{bv}} = 0.5\text{ m}$ — Đạt chuẩn Slide 30)
- **Vận tốc dòng chảy thượng lưu và tới gần ($v$, $v_{\text{app}}$)**: $0.43\text{ m/s}$ và $0.41\text{ m/s}$ (Kiểm tra: $v > 0.4\text{ m/s}$ — Đạt yêu cầu đề bài và Slide 29)
- **Số lượng thanh đan và số khe hở ($N_{\text{bars}}$, $N_{\text{spaces}}$)**: $62\text{ thanh}$ và $63\text{ khe}$ (Kiểm tra: $A_{\text{space}} = 0.56\text{ m}^2$ — Đạt chuẩn Slide 27)
- **Tổn thất cột nước sạch và tắc $50\%$ ($h_{L,\text{clean}}$, $h_{L,\text{clog}}$)**: $38\text{ mm}$ và $220\text{ mm}$ (Kiểm tra: $150 \le 220 \le 600\text{ mm}$ — Đạt chuẩn cơ giới Slide 29)
