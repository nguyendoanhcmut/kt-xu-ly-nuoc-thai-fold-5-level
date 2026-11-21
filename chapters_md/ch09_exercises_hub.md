### Bài tập ch09_ex01 (Slide 12, Trang 6): Ước tính Lượng Photpho Loại bỏ bằng Quá trình Sinh học Tăng cường (EBPR)

**Đề bài** (Lời giải khôi phục theo chuẩn slide của thầy từ Slide 11–12): Ước tính lượng photpho được loại bỏ và nồng độ photpho đầu ra của hệ thống khử photpho sinh học tăng cường (EBPR) vận hành ở tuổi bùn $\theta_c = 5\text{ d}$ xử lý dòng nước thải có tổng $\text{COD} = 300\text{ g/m}^3$, $\text{bCOD} = 200\text{ g/m}^3$, $\text{rbCOD} = 50\text{ g/m}^3$ và tổng photpho đầu vào $\text{P}_0 = 6.0\text{ g/m}^3$ [Page 6].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Tổng nhu cầu oxy hóa học đầu vào | $\text{COD}$ | $300$ | $\text{g/m}^3\text{ (Slide 12)}$ |
| Cơ chất dễ phân hủy sinh học | $\text{bCOD}$ | $200$ | $\text{g/m}^3\text{ (Slide 12)}$ |
| Cơ chất phân hủy sinh học nhanh | $\text{rbCOD}$ | $50$ | $\text{g/m}^3\text{ (Slide 12)}$ |
| Nồng độ Photpho tổng đầu vào | $\text{P}_0$ | $6.0$ | $\text{g/m}^3\text{ (Slide 12)}$ |
| Tỷ lệ chuyển hóa $\text{rbCOD}$ thành axetat | $\eta_{\text{ac}}$ | $90\%$ | $\%\text{ (Slide 12)}$ |
| Hệ số sản lượng tổng hợp vi khuẩn | $Y$ | $0.45$ | $\text{g VSS/g COD}\text{ (Slide 12)}$ |
| Hệ số phân hủy nội bào | $k_d$ | $0.08$ | $\text{g VSS/g VSS}\cdot\text{d}\text{ (Slide 12)}$ |
| Thời gian lưu bùn thiết kế | $\theta_c$ | $5.0$ | $\text{d}\text{ (Slide 12)}$ |
| Hàm lượng photpho trong vi khuẩn PAOs | $f_{\text{P,PAO}}$ | $0.30$ | $\text{g P/g VSS}\text{ (Slide 12)}$ |
| Hàm lượng photpho trong vi khuẩn khác | $f_{\text{P,other}}$ | $0.02$ | $\text{g P/g VSS}\text{ (Slide 12)}$ |
| Nồng độ cặn bay hơi đầu ra bể lắng | $\text{VSS}_e$ | $8.0$ | $\text{g/m}^3\text{ (Slide 12)}$ |

**Bước 1 - Xác định hệ số sản lượng quan sát $Y_{\text{obs}}$ và phân bố cơ chất**: Ở tuổi bùn $\theta_c = 5\text{ d}$, hệ số sản lượng sinh khối quan sát $Y_{\text{obs}}$ đạt $0.3214\text{ g VSS/g bCOD}$. Lượng cơ chất $\text{bCOD}_{\text{PAO}}$ do vi khuẩn PAOs hấp thụ dưới dạng axetat bằng $45.0\text{ g/m}^3$, và phần còn lại $\text{bCOD}_{\text{other}}$ cho vi khuẩn dị dưỡng khác bằng $155.0\text{ g/m}^3$ [Page 6].

$$Y_{\text{obs}} = \frac{Y}{1 + k_d \theta_c}$$

$$Y_{\text{obs}} = \frac{0.45}{1 + 0.08\times 5.0} = \frac{0.45}{1.40} = 0.3214\text{ g VSS/g bCOD}$$

$$\text{bCOD}_{\text{PAO}} = 0.90\times 50.0 = 45.0\text{ g/m}^3$$

$$\text{bCOD}_{\text{other}} = 200.0 - 45.0 = 155.0\text{ g/m}^3$$

**Bước 2 - Tính nồng độ sinh khối tạo thành trên một đơn vị lưu lượng**: Sinh khối vi khuẩn tích lũy photpho tạo thành $\Delta X_{\text{PAO}}$ đạt $14.46\text{ g VSS/m}^3$ và sinh khối vi khuẩn dị dưỡng khác $\Delta X_{\text{other}}$ đạt $49.82\text{ g VSS/m}^3$. Tổng nồng độ sinh khối tạo thành $\Delta X_{\text{tot}}$ bằng $64.29\text{ g VSS/m}^3$ [Page 6].

$$\Delta X_{\text{PAO}} = Y_{\text{obs}}\times \text{bCOD}_{\text{PAO}} = 0.3214\times 45.0 = 14.46\text{ g VSS/m}^3$$

$$\Delta X_{\text{other}} = 0.3214\times 155.0 = 49.82\text{ g VSS/m}^3$$

$$\Delta X_{\text{tot}} = 14.46 + 49.82 = 64.29\text{ g VSS/m}^3$$

**Bước 3 - Tính lượng photpho hấp thụ bởi vi khuẩn PAOs và vi khuẩn khác**: Lượng photpho được loại bỏ nhờ cơ chế tích lũy polyphosphate của PAOs đạt $\text{P}_{\text{PAO}}$ bằng $4.34\text{ g P/m}^3$, và lượng photpho đồng hóa bởi các vi khuẩn khác đạt $\text{P}_{\text{other}}$ bằng $1.00\text{ g P/m}^3$. Tổng lượng photpho hòa tan được sinh khối hấp thụ $\text{P}_{\text{uptake}}$ đạt $5.34\text{ g P/m}^3$ [Page 6].

$$\text{P}_{\text{PAO}} = \Delta X_{\text{PAO}}\times f_{\text{P,PAO}} = 14.46\times 0.30 = 4.34\text{ g P/m}^3$$

$$\text{P}_{\text{other}} = 49.82\times 0.02 = 1.00\text{ g P/m}^3$$

$$\text{P}_{\text{uptake}} = 4.34 + 1.00 = 5.34\text{ g P/m}^3$$

**Bước 4 - Xác định nồng độ photpho hòa tan và tổng photpho ở dòng ra**: Nồng độ photpho hòa tan còn lại ở dòng ra $\text{P}_{\text{sol,e}}$ bằng $0.66\text{ g P/m}^3$. Với hàm lượng photpho trung bình trong bùn $f_{\text{P,avg}}$ bằng $0.083\text{ g P/g VSS}$, lượng photpho dạng hạt trôi theo $\text{VSS}_e$ bằng $8.0\text{ g/m}^3$ là $\text{P}_{\text{part,e}}$ bằng $0.66\text{ g P/m}^3$ và tổng photpho đầu ra $\text{P}_{\text{tot,e}}$ bằng $1.32\text{ g P/m}^3$ [Page 6].

$$\text{P}_{\text{sol,e}} = \text{P}_0 - \text{P}_{\text{uptake}} = 6.00 - 5.34 = 0.66\text{ g P/m}^3$$

$$f_{\text{P,avg}} = \frac{5.34}{64.29} = 0.083\text{ g P/g VSS}$$

$$\text{P}_{\text{part,e}} = \text{VSS}_e\times f_{\text{P,avg}} = 8.0\times 0.083 = 0.66\text{ g P/m}^3$$

$$\text{P}_{\text{tot,e}} = 0.66 + 0.66 = 1.32\text{ g P/m}^3$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Hệ số sản lượng sinh khối quan sát ($Y_{\text{obs}}$)**: $0.3214\text{ g VSS/g bCOD}$ (Kiểm tra: $\theta_c = 5.0\text{ d} \in [2,\; 5]\text{ d cho hệ A/O - Đạt chuẩn Slide 21}$)
- **Sinh khối PAOs và vi khuẩn khác ($\Delta X_{\text{PAO}},\; \Delta X_{\text{other}}$)**: $14.46\text{ g VSS/m}^3,\; 49.82\text{ g VSS/m}^3$ (Kiểm tra: $\Delta X_{\text{tot}} = 64.29\text{ g VSS/m}^3\text{ - Đạt chuẩn Slide 12}$)
- **Tổng lượng photpho hấp thụ vào sinh khối ($\text{P}_{\text{uptake}}$)**: $5.34\text{ g P/m}^3$ (Kiểm tra: $\text{rbCOD}/\text{P}_{\text{PAO}} = 11.5\text{ g/g}\text{ - Đạt chuẩn Slide 11}$)
- **Nồng độ photpho hòa tan đầu ra ($\text{P}_{\text{sol,e}}$)**: $0.66\text{ g P/m}^3$ (Kiểm tra: $\text{P}_{\text{sol,e}} < 1.0\text{ g P/m}^3\text{ - Đạt chuẩn Slide 12}$)
- **Nồng độ photpho tổng cộng đầu ra ($\text{P}_{\text{tot,e}}$)**: $1.32\text{ g P/m}^3$ (Kiểm tra: $\text{P}_{\text{net}} = 4.68\text{ g P/m}^3\text{ - Đạt chuẩn Slide 12}$)

### Bài tập ch09_ex02 (Slide 22–23, Trang 10–11): Xác định Nồng độ Photpho Đầu ra và Hàm lượng Photpho trong Bùn Thải Hệ A2O

**Đề bài** (Lời giải khôi phục theo chuẩn slide của thầy từ Slide 19–23): Hệ thống xử lý sinh học A2O công suất $Q = 4000\text{ m}^3/\text{d}$ vận hành ở nhiệt độ $T = 12^\circ\text{C}$, tuổi bùn $\theta_c = 8\text{ d}$ và tỷ lệ tuần hoàn bùn $R = 0.5$. Hãy xác định nồng độ photpho hòa tan đầu ra $\text{P}_e$ và hàm lượng phần trăm photpho trong bùn dư xả bỏ [Page 10].

| Thông số thiết kế | Ký hiệu | Giá trị | Đơn vị và Nguồn Slide |
| :--- | :--- | :--- | :--- |
| Lưu lượng nước thải đầu vào | $Q$ | $4000$ | $\text{m}^3/\text{d}\text{ (Slide 22)}$ |
| Tổng nhu cầu oxy sinh hóa | $\text{BOD}$ | $160$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Cơ chất dễ phân hủy sinh học | $\text{bCOD}$ | $250$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Cơ chất phân hủy sinh học nhanh | $\text{rbCOD}$ | $75$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Nồng độ axetat đầu vào | $S_{\text{ac}}$ | $15$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Cặn bay hơi không phân hủy sinh học | $\text{nbVSS}$ | $20$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Chất rắn trơ vô cơ đầu vào | $\text{iTSS}$ | $10$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Tổng Nitơ Kjeldahl và Photpho đầu vào | $\text{TKN},\; \text{P}_0$ | $35,\; 6.0$ | $\text{g/m}^3\text{ (Slide 22)}$ |
| Nhiệt độ vận hành hệ thống | $T$ | $12$ | $^\circ\text{C}\text{ (Slide 22)}$ |
| Tỷ lệ tuần hoàn bùn hoạt tính | $R$ | $0.50$ | $\text{m}^3/\text{m}^3\text{ (Slide 23)}$ |
| Thời gian lưu bùn thiết kế | $\theta_c$ | $8.0$ | $\text{d}\text{ (Slide 23)}$ |
| Nitrat sinh ra và nitrat đầu ra | $\text{NO}_x,\; \text{NO}_{x,e}$ | $28,\; 6.0$ | $\text{g/m}^3\text{ (Slide 23)}$ |
| Hàm lượng photpho trong vi khuẩn khác | $f_{\text{P,other}}$ | $0.015$ | $\text{g P/g VSS}\text{ (Slide 23)}$ |
| Định mức $\text{rbCOD}$ tiêu tốn do nitrat | $\eta_{\text{NO}_3}$ | $5.2$ | $\text{g rbCOD/g NO}_3\text{-N}\text{ (Slide 20)}$ |

**Bước 1 - Tính lượng $\text{rbCOD}$ bị tiêu hao bởi nitrat tuần hoàn vào bể kỵ khí**: Dòng bùn tuần hoàn $R = 0.5$ mang nitrat ở nồng độ $\text{NO}_{x,e}$ bằng $6.0\text{ g/m}^3$ về bể kỵ khí, tương ứng tải lượng $3.0\text{ g/m}^3$ dòng vào. Với định mức $5.2\text{ g/g}$ trên Slide 20, lượng $\text{rbCOD}$ còn lại cho PAOs đạt $59.4\text{ g/m}^3$ [Page 9].

$$\text{NO}_3\text{-N}_{\text{an}} = R\times \text{NO}_{x,e} = 0.50\times 6.0 = 3.0\text{ g/m}^3$$

$$\text{rbCOD}_{\text{NO}_3} = 5.2\times 3.0 = 15.6\text{ g/m}^3$$

$$\text{rbCOD}_{\text{EBPR}} = 75.0 - 15.6 = 59.4\text{ g/m}^3$$

**Bước 2 - Xác định lượng photpho loại bỏ nhờ cơ chế EBPR của vi khuẩn PAOs**: Tỷ số $\text{VFA}/\text{rbCOD}$ đầu vào bằng $0.20$. Tra đồ thị trên Slide 19 tại $\text{VFA}/\text{rbCOD} = 0.20$ được định mức tiêu thụ cơ chất bằng $14.5\text{ g rbCOD/g P}$ (hoặc $15.0\text{ g/g}$), suy ra lượng photpho khử bởi PAOs đạt $\text{P}_{\text{EBPR}}$ bằng $4.10\text{ g P/m}^3$ [Page 9].

$$\frac{\text{VFA}}{\text{rbCOD}} = \frac{15.0}{75.0}$$

$$\frac{\text{VFA}}{\text{rbCOD}} = 0.20 \implies \text{Tỷ số }\frac{\text{rbCOD}}{\text{P}} = 14.5\text{ g rbCOD/g P}$$

$$\text{P}_{\text{EBPR}} = \frac{\text{rbCOD}_{\text{EBPR}}}{14.5} = \frac{59.4}{14.5} = 4.10\text{ g P/m}^3$$

**Bước 3 - Tính lượng photpho đồng hóa bởi vi khuẩn dị dưỡng khác và nitrat hóa ở $12^\circ\text{C}$**: Hiệu chỉnh nhiệt độ về $12^\circ\text{C}$ cho $k_{d,H} = 0.0731\text{ d}^{-1}$ và $k_{d,n} = 0.0585\text{ d}^{-1}$. Sinh khối hoạt động của vi khuẩn dị dưỡng khác $\Delta X_{H,\text{act}}$ đạt $54.13\text{ g/m}^3$ và vi khuẩn nitrat hóa $\Delta X_{n,\text{act}}$ đạt $2.29\text{ g/m}^3$, tiêu thụ lượng photpho tổng hợp tế bào $\text{P}_{\text{synth}}$ bằng $0.85\text{ g P/m}^3$ [Page 11].

$$k_{d,H(12)} = 0.10\times (1.04)^{12-20} = 0.0731\text{ d}^{-1}$$

$$k_{d,n(12)} = 0.08\times (1.04)^{12-20} = 0.0585\text{ d}^{-1}$$

$$\Delta X_{H,\text{act}} = \frac{0.45\times (250.0 - 59.4)}{1 + 0.0731\times 8.0} = 54.13\text{ g/m}^3$$

$$\Delta X_{n,\text{act}} = \frac{0.12\times 28.0}{1 + 0.0585\times 8.0} = 2.29\text{ g/m}^3$$

$$\text{P}_{\text{synth}} = f_{\text{P,other}}(\Delta X_{H,\text{act}} + \Delta X_{n,\text{act}})$$

$$\text{P}_{\text{synth}} = 0.015\times (54.13 + 2.29) = 0.85\text{ g P/m}^3$$

**Bước 4 - Xác định nồng độ photpho đầu ra $\text{P}_e$ và khối lượng photpho thu hồi**: Tổng lượng photpho loại bỏ $\text{P}_{\text{rem}}$ đạt $4.95\text{ g P/m}^3$, nên nồng độ photpho hòa tan còn lại ở dòng ra $\text{P}_e$ bằng $1.05\text{ g P/m}^3$ (hoặc $1.19\text{ g P/m}^3$ nếu lấy tỷ số bằng $15.0$). Khối lượng photpho tích lũy trong bùn dư mỗi ngày $M_{\text{P}}$ đạt $19.80\text{ kg P/d}$ [Page 11].

$$\text{P}_{\text{rem}} = \text{P}_{\text{EBPR}} + \text{P}_{\text{synth}} = 4.10 + 0.85 = 4.95\text{ g P/m}^3$$

$$\text{P}_e = \text{P}_0 - \text{P}_{\text{rem}} = 6.00 - 4.95 = 1.05\text{ g P/m}^3$$

$$M_{\text{P}} = \frac{4000\times 4.95}{10^3} = 19.80\text{ kg P/d}$$

**Bước 5 - Tính tổng lượng bùn thải và hàm lượng phần trăm photpho trong bùn**: Cộng toàn bộ sinh khối tạo thành $P_{x,\text{bio}}$ bằng $318.7\text{ kg VSS/d}$ với $\text{nbVSS}$ ($80.0\text{ kg/d}$) và $\text{iTSS}$ ($40.0\text{ kg/d}$), tổng lượng bùn thải đạt $P_{x,\text{VSS}}$ bằng $398.7\text{ kg VSS/d}$ và $P_{x,\text{TSS}}$ bằng $494.9\text{ kg TSS/d}$. Hàm lượng photpho trong bùn thải đạt $4.96\%\text{ P/VSS}$ và $4.00\%\text{ P/TSS}$ [Page 11].

$$P_{x,\text{VSS}} = P_{x,\text{bio}} + \frac{Q\cdot \text{nbVSS}}{10^3} = 318.7 + 80.0 = 398.7\text{ kg VSS/d}$$

$$P_{x,\text{TSS}} = \frac{318.7}{0.85} + 80.0 + 40.0 = 494.9\text{ kg TSS/d}$$

$$\%\text{P}_{\text{VSS}} = \frac{19.80}{398.7}\times 100\% = 4.96\%$$

$$\%\text{P}_{\text{TSS}} = \frac{19.80}{494.9}\times 100\% = 4.00\%$$

**Tổng hợp đáp số và kiểm tra điều kiện biên**: Toàn bộ thông số thiết kế thỏa mãn giới hạn tiêu chuẩn trên slide bài giảng của TS. Nguyễn Hoàng Dũng.

- **Tỷ số $\text{BOD}/\text{P}$ và thông số vận hành ($R,\; \theta_c$)**: $\text{BOD}/\text{P} = 26.7,\; R = 50\%,\; \theta_c = 8.0\text{ d}$ (Kiểm tra: $R \in [25\%,\; 100\%],\; \theta_c \in [5,\; 25]\text{ d - Đạt chuẩn Slide 21}$)
- **Lượng $\text{rbCOD}$ hữu hiệu cho PAOs ($\text{rbCOD}_{\text{EBPR}}$)**: $59.4\text{ g/m}^3$ (Kiểm tra: $\text{rbCOD}_{\text{NO}_3} = 15.6\text{ g/m}^3\text{ - Đạt chuẩn Slide 20}$)
- **Tổng lượng photpho được loại bỏ ($\text{P}_{\text{rem}},\; M_{\text{P}}$)**: $4.95\text{ g P/m}^3,\; 19.80\text{ kg P/d}$ (Kiểm tra: $\text{P}_{\text{EBPR}} = 4.10\text{ g/m}^3,\; \text{P}_{\text{synth}} = 0.85\text{ g/m}^3\text{ - Đạt chuẩn Slide 19}$)
- **Nồng độ photpho hòa tan đầu ra ($\text{P}_e$)**: $1.05\text{ g P/m}^3$ (Kiểm tra: $\text{Hiệu suất khử P} = 82.5\%\text{ - Đạt chuẩn Slide 23}$)
- **Hàm lượng photpho trong bùn dư xả bỏ ($\%\text{P}_{\text{VSS}},\; \%\text{P}_{\text{TSS}}$)**: $4.96\%\text{ P/VSS},\; 4.00\%\text{ P/TSS}$ (Kiểm tra: $P_{x,\text{VSS}} = 398.7\text{ kg/d},\; P_{x,\text{TSS}} = 494.9\text{ kg/d - Đạt chuẩn Slide 23}$)
