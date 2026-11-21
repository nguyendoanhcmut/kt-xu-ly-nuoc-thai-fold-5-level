### Bài tập ch01_ex01 (Slide 50 - Example 1): Xác định BOD 1 ngày, UBOD và quy đổi BOD5 theo nhiệt độ

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Một mẫu nước thải có nhu cầu oxy sinh hóa sau $5\text{ ngày}$ ở nhiệt độ $T_1 = 20^\circ\text{C}$ là $\text{BOD}_5 = 200\text{ mg/L}$ [Page 25]. Biết hằng số tốc độ phản ứng bậc nhất (cơ số $e$) ở $20^\circ\text{C}$ là $k_{20} = 0.23\text{ ngày}^{-1}$ và hệ số nhiệt độ $\theta = 1.047$ [Page 23] [Page 25]. Hãy xác định nhu cầu oxy sinh hóa hoàn toàn $\text{UBOD}$, nhu cầu oxy sinh hóa sau $1\text{ ngày}$ ($\text{BOD}_1$) ở $20^\circ\text{C}$, và giá trị $\text{BOD}_5$ nếu thí nghiệm được thực hiện ở nhiệt độ $T_2 = 25^\circ\text{C}$ [Page 25].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Nhu cầu oxy sinh hóa $5\text{ ngày}$ ở $20^\circ\text{C}$ | $\text{BOD}_{5,20}$ | $200$ | $\text{mg/L}$ (Slide 50) |
| Hằng số tốc độ phản ứng ở $20^\circ\text{C}$ | $k_{20}$ | $0.23$ | $\text{ngày}^{-1}$ (Slide 50) |
| Hệ số hiệu chỉnh nhiệt độ Arrhenius | $\theta$ | $1.047$ | $\text{Không thứ nguyên}$ (Slide 46, 50) |
| Nhiệt độ thí nghiệm tiêu chuẩn và quy đổi | $T_1, T_2$ | $20, 25$ | $^\circ\text{C}$ (Slide 50) |

**Bước 1 - Xác định nhu cầu oxy sinh hóa hoàn toàn $\text{UBOD}$ ở $20^\circ\text{C}$**: Áp dụng phương trình động học bậc nhất tại thời điểm $t = 5\text{ ngày}$ với $\text{BOD}_{5,20} = 200\text{ mg/L}$ và $k_{20} = 0.23\text{ ngày}^{-1}$ để tính $\text{UBOD} = 292.67\text{ mg/L}$ [Page 23] [Page 25].

$$
\text{UBOD} = \frac{\text{BOD}_{5,20}}{1 - e^{-5 \cdot k_{20}}} = \frac{200}{1 - e^{-5 \times 0.23}}
$$

$$
\text{UBOD} = \frac{200}{1 - 0.3166} = 292.67\text{ (mg/L)}
$$

**Bước 2 - Tính nhu cầu oxy sinh hóa sau $1\text{ ngày}$ ($\text{BOD}_1$) ở $20^\circ\text{C}$**: Thay giá trị $\text{UBOD} = 292.67\text{ mg/L}$ và thời gian $t = 1\text{ ngày}$ vào phương trình động học bậc nhất, thu được $\text{BOD}_{1,20} = 60.13\text{ mg/L}$ [Page 23].

$$
\text{BOD}_{1,20} = \text{UBOD} \cdot \left(1 - e^{-1 \cdot k_{20}}\right) = 292.67 \times \left(1 - e^{-0.23}\right)
$$

$$
\text{BOD}_{1,20} = 292.67 \times \left(1 - 0.7945\right) = 60.13\text{ (mg/L)}
$$

**Bước 3 - Quy đổi hằng số tốc độ phản ứng sang nhiệt độ $25^\circ\text{C}$**: Áp dụng công thức van't Hoff-Arrhenius với hệ số $\theta = 1.047$ để xác định hằng số tốc độ ở $25^\circ\text{C}$ là $k_{25} = 0.2894\text{ ngày}^{-1}$ [Page 23] [Page 25].

$$
\frac{k_{25}}{k_{20}} = \theta^{T_2 - T_1} \implies k_{25} = k_{20} \cdot \theta^{25 - 20}
$$

$$
k_{25} = 0.23 \times (1.047)^5 = 0.2894\text{ (ngày}^{-1}\text{)}
$$

**Bước 4 - Tính nhu cầu oxy sinh hóa $\text{BOD}_5$ ở nhiệt độ $25^\circ\text{C}$**: Thay $\text{UBOD} = 292.67\text{ mg/L}$ và $k_{25} = 0.2894\text{ ngày}^{-1}$ vào phương trình tại $t = 5\text{ ngày}$, thu được $\text{BOD}_{5,25} = 223.80\text{ mg/L}$ [Page 25].

$$
\text{BOD}_{5,25} = \text{UBOD} \cdot \left(1 - e^{-5 \cdot k_{25}}\right) = 292.67 \times \left(1 - e^{-5 \times 0.2894}\right)
$$

$$
\text{BOD}_{5,25} = 292.67 \times \left(1 - 0.2353\right) = 223.80\text{ (mg/L)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Nhu cầu oxy sinh hóa hoàn toàn ($\text{UBOD}$)**: $292.67\text{ mg/L}$ (Kiểm tra: $\text{UBOD} > \text{BOD}_{5,20} = 200\text{ mg/L}\text{ — Đạt chuẩn Slide 46}$)
- **Nhu cầu oxy sinh hóa $1\text{ ngày}$ ở $20^\circ\text{C}$ ($\text{BOD}_{1,20}$)**: $60.13\text{ mg/L}$ (Kiểm tra: $\text{BOD}_{1,20} < \text{BOD}_{5,20} = 200\text{ mg/L}\text{ — Đạt chuẩn Slide 50}$)
- **Hằng số tốc độ phản ứng ở $25^\circ\text{C}$ ($k_{25}$)**: $0.2894\text{ ngày}^{-1}$ (Kiểm tra: $k_{25} > k_{20} = 0.23\text{ ngày}^{-1}\text{ — Đạt chuẩn Slide 46}$)
- **Nhu cầu oxy sinh hóa $5\text{ ngày}$ ở $25^\circ\text{C}$ ($\text{BOD}_{5,25}$)**: $223.80\text{ mg/L}$ (Kiểm tra: $60.13 < 200 < 223.80 < 292.67\text{ mg/L}\text{ — Đạt chuẩn Slide 50}$)

### Bài tập ch01_ex02 (Slide 52 - Example 2): Phân đoạn các thành phần nhu cầu oxy hóa học COD

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Một mẫu nước thải có các thông số chất lượng đầu vào gồm $\text{BOD} = 200\text{ mg/L}$, tổng nhu cầu oxy hóa học $\text{COD} = 420\text{ mg/L}$, phần $\text{COD}$ phân hủy sinh học nhanh $\text{rbCOD} = 80\text{ mg/L}$ và phần $\text{COD}$ hòa tan không phân hủy sinh học $\text{nbsCOD} = 30\text{ mg/L}$ [Page 26]. Hãy xác định nồng độ $\text{COD}$ phân hủy sinh học ($\text{bCOD}$), $\text{COD}$ dạng hạt không phân hủy sinh học ($\text{nbpCOD}$) và $\text{COD}$ phân hủy sinh học chậm ($\text{sbCOD}$) [Page 25] [Page 26].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Nhu cầu oxy sinh hóa tiêu chuẩn | $\text{BOD}$ | $200$ | $\text{mg/L}$ (Slide 52) |
| Tổng nhu cầu oxy hóa học | $\text{COD}$ | $420$ | $\text{mg/L}$ (Slide 52) |
| $\text{COD}$ phân hủy sinh học nhanh | $\text{rbCOD}$ | $80$ | $\text{mg/L}$ (Slide 52) |
| $\text{COD}$ hòa tan không phân hủy sinh học | $\text{nbsCOD}$ | $30$ | $\text{mg/L}$ (Slide 52) |
| Hệ số quy đổi $\text{bCOD}$ theo $\text{BOD}$ | $\frac{\text{bCOD}}{\text{BOD}}$ | $1.6$ | $\text{Không thứ nguyên}$ (Slide 49) |

**Bước 1 - Xác định nồng độ $\text{COD}$ phân hủy sinh học ($\text{bCOD}$)**: Áp dụng tỷ lệ thực nghiệm $\text{bCOD} = 1.6 \cdot \text{BOD}$ trên Slide 49 với $\text{BOD} = 200\text{ mg/L}$, tính được $\text{bCOD} = 320\text{ mg/L}$ [Page 25] [Page 26].

$$
\frac{\text{bCOD}}{\text{BOD}} = 1.6 \implies \text{bCOD} = 1.6 \times 200 = 320\text{ (mg/L)}
$$

**Bước 2 - Xác định nồng độ $\text{COD}$ không phân hủy sinh học tổng cộng ($\text{nbCOD}$)**: Áp dụng phương trình cân bằng tổng $\text{COD}$ để tìm $\text{nbCOD} = 100\text{ mg/L}$ [Page 25].

$$
\text{nbCOD} = \text{COD} - \text{bCOD} = 420 - 320 = 100\text{ (mg/L)}
$$

**Bước 3 - Xác định nồng độ $\text{COD}$ dạng hạt không phân hủy sinh học ($\text{nbpCOD}$)**: Lấy $\text{nbCOD} = 100\text{ mg/L}$ trừ đi phần hòa tan $\text{nbsCOD} = 30\text{ mg/L}$, thu được $\text{nbpCOD} = 70\text{ mg/L}$ [Page 25] [Page 26].

$$
\text{nbpCOD} = \text{nbCOD} - \text{nbsCOD} = 100 - 30 = 70\text{ (mg/L)}
$$

**Bước 4 - Xác định nồng độ $\text{COD}$ phân hủy sinh học chậm ($\text{sbCOD}$)**: Lấy $\text{bCOD} = 320\text{ mg/L}$ trừ đi phần phân hủy nhanh $\text{rbCOD} = 80\text{ mg/L}$, thu được $\text{sbCOD} = 240\text{ mg/L}$ [Page 25] [Page 26].

$$
\text{sbCOD} = \text{bCOD} - \text{rbCOD} = 320 - 80 = 240\text{ (mg/L)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Nồng độ $\text{COD}$ phân hủy sinh học ($\text{bCOD}$)**: $320\text{ mg/L}$ (Kiểm tra: $\frac{\text{bCOD}}{\text{BOD}} = \frac{320}{200} = 1.6\text{ — Đạt chuẩn Slide 49}$)
- **Nồng độ $\text{COD}$ không phân hủy sinh học ($\text{nbCOD}$)**: $100\text{ mg/L}$ (Kiểm tra: $\text{bCOD} + \text{nbCOD} = 320 + 100 = 420\text{ mg/L}\text{ — Đạt chuẩn Slide 49}$)
- **Nồng độ $\text{COD}$ dạng hạt không phân hủy ($\text{nbpCOD}$)**: $70\text{ mg/L}$ (Kiểm tra: $\text{nbpCOD} + \text{nbsCOD} = 70 + 30 = 100\text{ mg/L}\text{ — Đạt chuẩn Slide 52}$)
- **Nồng độ $\text{COD}$ phân hủy sinh học chậm ($\text{sbCOD}$)**: $240\text{ mg/L}$ (Kiểm tra: $240 + 80 + 70 + 30 = 420\text{ mg/L}\text{ — Đạt chuẩn Slide 52}$)

### Bài tập ch01_ex03 (Slide 81 - Example 3): Xác định nồng độ COD tối đa cho phép xả vào hồ theo QCVN 40:2011/BTNMT

**Đề bài** ([Lời giải khôi phục theo chuẩn slide của thầy]): Một nhà máy xả nước thải công nghiệp với lưu lượng $F = 100\text{ m}^3\text{/ngày}$ vào một hồ tiếp nhận có dung tích $V = 100,000\text{ m}^3$ [Page 40]. Hồ nước này không sử dụng cho mục đích cấp nước sinh hoạt [Page 40]. Hãy áp dụng quy chuẩn kỹ thuật quốc gia QCVN 40:2011/BTNMT để xác định nồng độ $\text{COD}$ tối đa cho phép ($C_{\max}$) trong nước thải xả ra hồ [Page 36] [Page 39] [Page 40].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng xả nước thải công nghiệp | $F$ | $100$ | $\text{m}^3\text{/ngày}$ (Slide 81) |
| Dung tích hồ tiếp nhận nước thải | $V$ | $100,000$ | $\text{m}^3$ (Slide 81) |
| Giá trị cơ sở của $\text{COD}$ tại Cột B | $C$ | $150$ | $\text{mg/L}$ (Bảng 1, Slide 74) |
| Hệ số dung tích hồ tiếp nhận | $K_q$ | $0.6$ | $\text{Không thứ nguyên}$ (Bảng 3, Slide 79) |
| Hệ số lưu lượng nguồn thải | $K_f$ | $1.1$ | $\text{Không thứ nguyên}$ (Bảng 4, Slide 80) |

**Bước 1 - Tra giá trị nồng độ cơ sở $C$ của thông số $\text{COD}$**: Do hồ tiếp nhận không dùng cho mục đích cấp nước sinh hoạt, tra Cột B tại Bảng 1 của QCVN 40:2011/BTNMT thu được $C = 150\text{ mg/L}$ [Page 36].

$$
C_{\text{COD, Cột B}} = 150\text{ (mg/L)}
$$

**Bước 2 - Xác định hệ số nguồn tiếp nhận $K_q$ và hệ số lưu lượng $K_f$**: Với dung tích hồ $V = 0.1 \times 10^6\text{ m}^3 \le 10 \times 10^6\text{ m}^3$, tra Bảng 3 được $K_q = 0.6$, và với lưu lượng $50 < F = 100 \le 500\text{ m}^3\text{/ngày}$, tra Bảng 4 được $K_f = 1.1$ [Page 39].

$$
\begin{cases}
V = 100,000\text{ m}^3 \le 10 \times 10^6\text{ m}^3 \implies K_q = 0.6 \\
50\text{ m}^3\text{/ngày} < F = 100\text{ m}^3\text{/ngày} \le 500\text{ m}^3\text{/ngày} \implies K_f = 1.1
\end{cases}
$$

**Bước 3 - Tính nồng độ $\text{COD}$ tối đa cho phép xả ra hồ ($C_{\max}$)**: Nhân giá trị chuẩn $C = 150\text{ mg/L}$ với hai hệ số $K_q = 0.6$ và $K_f = 1.1$, thu được $C_{\max} = 99\text{ mg/L}$ [Page 36] [Page 40].

$$
C_{\max} = C \times K_q \times K_f = 150 \times 0.6 \times 1.1 = 99\text{ (mg/L)}
$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của Tiến sĩ Nguyễn Hoàng Dũng.

- **Giá trị cơ sở Cột B của $\text{COD}$ ($C$)**: $150\text{ mg/L}$ (Kiểm tra: $\text{Nguồn tiếp nhận không cấp nước sinh hoạt — Đạt chuẩn Slide 74}$)
- **Hệ số dung tích hồ tiếp nhận ($K_q$)**: $0.6$ (Kiểm tra: $V = 10^5\text{ m}^3 \le 10^7\text{ m}^3\text{ — Đạt chuẩn Slide 79}$)
- **Hệ số lưu lượng nguồn thải ($K_f$)**: $1.1$ (Kiểm tra: $50 < F = 100 \le 500\text{ m}^3\text{/ngày}\text{ — Đạt chuẩn Slide 80}$)
- **Nồng độ $\text{COD}$ tối đa cho phép ($C_{\max}$)**: $99\text{ mg/L}$ (Kiểm tra: $C_{\max} = 99\text{ mg/L} < C = 150\text{ mg/L}\text{ — Đạt chuẩn Slide 81}$)
