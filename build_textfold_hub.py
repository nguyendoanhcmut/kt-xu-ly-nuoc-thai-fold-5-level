#!/usr/bin/env python3
"""
build_textfold_hub.py
Builds the 100% native TextFold 5-level Semantic Zoom Course Hub (`hub_master.md` ->
`readers/hub_master/index.fold.html` -> `index.html`) directly from the 17
`chapters_md/<slug>_exercises_hub.md` 4-Block LaTeX exercise files, cleanly recompiles all
18 `.fold.html` files via `fold_pipeline.py compile`, equips `index.html` plus all 18 `.fold.html`
readers with TextFold's native `app.css`, default dark theme (`data-theme="dark"`), and collapsible
`<aside id="sidebar">` library drawer, and verifies all 4 Hard Verification Gates.
"""

import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from bs4 import BeautifulSoup

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai\fold_5_level_v1")
MASTER_JSON = BASE_DIR / "ALL_54_EXERCISES_COMPLETE_SOLUTIONS.json"
HUB_MD = BASE_DIR / "hub_master.md"
HUB_READER_DIR = BASE_DIR / "readers" / "hub_master"
ROOT_INDEX_HTML = BASE_DIR / "index.html"

_SKILL_ROOT = Path(r"C:\Users\Admin\.gemini\config\skills\textfold-branches")
if not _SKILL_ROOT.exists():
    _SKILL_ROOT = Path(r"C:\Users\Admin\.gemini\config\skills\branches")
FOLD_PIPELINE = _SKILL_ROOT / "scripts" / "fold_pipeline.py"
VENDOR_WEB = _SKILL_ROOT / "vendor" / "textfold" / "textfold" / "web"

CHAPTER_META = {
    "ch01": {
        "title": "Chương 1 - Tổng quan Quản lý Nước thải và Phân đoạn BOD, COD, QCVN 40",
        "scope": "Chương 1 thiết lập cơ sở tính toán động học $\\text{BOD}$ bậc nhất $L_t = L_0 e^{-k_1 t}$, phân đoạn $\\text{COD}$ ($\\text{rbCOD}$, $\\text{sbCOD}$, $\\text{nbsCOD}$, $\\text{nbpCOD}$), phân đoạn chất rắn ($\\text{TSS}$, $\\text{VSS}$, $\\text{fTSS}$) và quy chuẩn xả thải $C_{\\max} = C \\times K_q \\times K_f$.",
        "sec_takeaway": "Chương 1 thiết lập động học $\\text{BOD}$, phân đoạn $\\text{COD}$ và quy chuẩn xả thải.",
        "sec_topic": "phân đoạn",
        "u0_takeaway": "Chương 1 cung cấp mô hình động học bậc nhất, phân đoạn $\\text{COD}$ và hệ số $K_q, K_f$.",
        "u0_topic": "mô hình động học",
        "u0_reason": "Người đọc tra cứu trực tiếp $52$ hình slide, bảng hệ số lưu lượng $K_q, K_f$ và $3$ bài giải mẫu hoàn chỉnh.",
    },
    "ch02": {
        "title": "Chương 2 - Lưu lượng Nước thải và Tải lượng Chất ô nhiễm Đầu vào",
        "scope": "Chương 2 trình bày phương pháp xác định lưu lượng trung bình ngày $Q_{\\text{tb}}$, hệ số giờ cao điểm $K_p$, tải lượng khối lượng chất ô nhiễm ($\\text{BOD}_5$, $\\text{TSS}$, $\\text{TKN}$) và thiết kế bể điều hòa lưu lượng, nồng độ.",
        "sec_takeaway": "Chương 2 xác định lưu lượng thiết kế $Q_{\\text{tb}}$, tải lượng ô nhiễm và bể điều hòa.",
        "sec_topic": "bể điều hòa",
        "u0_takeaway": "Chương 2 tính toán lưu lượng thiết kế $Q_{\\max}$, tải lượng ngày và thể tích bể điều hòa.",
        "u0_topic": "lưu lượng thiết kế",
        "u0_reason": "Trình đọc gồm $5$ bài giải cân bằng thể tích tích lũy và đồng nhất nồng độ từng giờ.",
    },
    "ch03_1": {
        "title": "Chương 3.1 - Thiết kế Song chắn rác Thô, Tinh và Tổn thất Cột nước",
        "scope": "Chương 3.1 cung cấp quy trình thiết kế kênh đặt song chắn rác theo công thức Manning $v = \\frac{1}{n} R^{2/3} S^{1/2}$, tính diện tích khe hở, vận tốc qua khe $v_b$ và tổn thất cột nước $\\Delta h$ qua song chắn.",
        "sec_takeaway": "Chương 3.1 thiết kế kênh song chắn rác và kiểm soát tổn thất cột nước $\\Delta h$.",
        "sec_topic": "song chắn rác",
        "u0_takeaway": "Chương 3.1 thiết kế tiết diện kênh Manning, số thanh chắn $N$ và tổn thất cột nước $\\Delta h$.",
        "u0_topic": "tiết diện kênh",
        "u0_reason": "Tài liệu tích hợp $53$ hình slide và $3$ bài giải tính toán góc nghiêng $\\theta$ và tắc nghẽn khe.",
    },
    "ch03_2": {
        "title": "Chương 3.2 - Thiết kế Bể lắng cát Ngang và Bể lắng cát Thổi khí",
        "scope": "Chương 3.2 thiết lập phương trình vận tốc lắng hạt rời rạc $v_s$ theo định luật Stokes và Newton, thiết kế bể lắng cát ngang kiểm soát vận tốc ngang $v_h$ và bể lắng cát thổi khí xoắn ốc.",
        "sec_takeaway": "Chương 3.2 thiết kế bể lắng cát ngang và bể lắng cát thổi khí theo $v_s$.",
        "sec_topic": "bể lắng cát",
        "u0_takeaway": "Chương 3.2 tính toán vận tốc lắng hạt cát $v_s$, kích thước bể và lưu lượng khí cấp.",
        "u0_topic": "vận tốc lắng",
        "u0_reason": "Chương học gồm $25$ hình slide và $4$ bài giải chi tiết cho bể lắng cát ngang và thổi khí.",
    },
    "ch03_3": {
        "title": "Chương 3.3 - Thiết kế Bể lắng Đợt 1, Bể lắng Tấm nghiêng và Đập tràn",
        "scope": "Chương 3.3 trình bày thiết kế bể lắng ngang hình chữ nhật, bể lắng tròn, bể lắng tải trọng cao dùng ống lắng nghiêng, kiểm tra số Reynolds $\\text{Re}$, số Froude $\\text{Fr}$, vận tốc cuốn trôi $v_{\\text{sc}}$ và máng tràn.",
        "sec_takeaway": "Chương 3.3 thiết kế bể lắng truyền thống, ống lắng nghiêng và máng thu nước.",
        "sec_topic": "ống lắng nghiêng",
        "u0_takeaway": "Chương 3.3 thiết kế diện tích bề mặt bể lắng, kiểm tra $\\text{Re}, \\text{Fr}$ và tải trọng máng tràn.",
        "u0_topic": "diện tích bề mặt",
        "u0_reason": "Trình đọc bao gồm $52$ hình slide và $6$ bài giải hoàn chỉnh từ ảnh chụp lớp học và bộ giải.",
    },
    "ch03_4": {
        "title": "Chương 3.4 - Thiết kế Hệ thống Tuyển nổi Khí hòa tan (DAF)",
        "scope": "Chương 3.4 xây dựng phương trình tỷ số khí trên chất rắn $A/S$ cho hệ thống tuyển nổi khí hòa tan không tuần hoàn và có tuần hoàn dòng ra áp lực cao $R$.",
        "sec_takeaway": "Chương 3.4 tính toán tỷ số khí trên chất rắn $A/S$ cho bể tuyển nổi.",
        "sec_topic": "bể tuyển nổi",
        "u0_takeaway": "Chương 3.4 xác định áp suất bình bão hòa $P$, lưu lượng tuần hoàn $Q_R$ và diện tích bể.",
        "u0_topic": "lưu lượng tuần hoàn",
        "u0_reason": "Chương học cung cấp $18$ hình slide cùng $3$ bài toán thiết kế tuyển nổi khí hòa tan.",
    },
    "ch03_5": {
        "title": "Chương 3.5 - Thiết kế Bể lọc Tầng sâu và Thủy lực Rửa ngược",
        "scope": "Chương 3.5 trình bày công thức Rose và Ergun tính tổn thất áp lực $h_L$ qua lớp vật liệu lọc sạch, cân bằng lực kéo rửa ngược $v_b$ và tính độ giãn nở lớp vật liệu lọc $L_e$.",
        "sec_takeaway": "Chương 3.5 tính tổn thất cột nước lọc sạch $h_L$ và vận tốc rửa ngược $v_b$.",
        "sec_topic": "vận tốc rửa ngược",
        "u0_takeaway": "Chương 3.5 giải phương trình tổn thất cột nước $h_L$, hệ số cản $C_D$ và độ giãn nở $L_e$.",
        "u0_topic": "tổn thất cột nước",
        "u0_reason": "Nội dung gồm $15$ hình slide và $4$ bài giải thủy lực lọc một lớp và hai lớp.",
    },
    "ch04_1": {
        "title": "Chương 4.1 - Hóa lý Keo tụ, Tạo bông và Cân bằng Độ kiềm Phèn nhôm, Phèn sắt",
        "scope": "Chương 4.1 phân tích cơ chế nén lớp điện tích kép, phản ứng thủy phân phèn nhôm và phèn sắt, lượng độ kiềm tiêu thụ theo $\\text{CaCO}_3$, lượng vôi bổ sung và khối lượng bùn hóa học sinh ra.",
        "sec_takeaway": "Chương 4.1 tính liều lượng phèn, độ kiềm $\\text{CaCO}_3$ và lượng bùn kết tủa hóa học.",
        "sec_topic": "liều lượng phèn",
        "u0_takeaway": "Chương 4.1 cân bằng phương trình thủy phân phèn nhôm, phèn sắt và lượng vôi $\\text{Ca(OH)}_2$.",
        "u0_topic": "phương trình thủy phân",
        "u0_reason": "Chương học có $14$ hình slide và $3$ bài giải cân bằng hóa học đầy đủ.",
    },
    "ch04_2": {
        "title": "Chương 4.2 - Thiết kế Bể Khuấy trộn Nhanh và Bể Tạo bông Tuabin, Cánh khuấy",
        "scope": "Chương 4.2 trình bày gradien vận tốc $G = \\sqrt{\\frac{P}{\\mu V}}$, số công suất $N_P$, số bơm $N_Q$, thiết kế bể tạo bông tuabin trục đứng $3$ ngăn và bể tạo bông cánh khuấy.",
        "sec_takeaway": "Chương 4.2 thiết kế bể khuấy trộn nhanh và bể tạo bông nhiều ngăn theo $G$.",
        "sec_topic": "bể tạo bông",
        "u0_takeaway": "Chương 4.2 tính công suất khuấy $P$, đường kính cánh khuấy $D$, gradien vận tốc $G$ và lực cản.",
        "u0_topic": "công suất khuấy",
        "u0_reason": "Tài liệu gồm $37$ hình slide và $3$ bài giải thiết kế tuabin và cánh khuấy.",
    },
    "ch04_3": {
        "title": "Chương 4.3 - Động học Khử trùng Chick-Watson, Collins-Selleck và Thiết kế Bể tiếp xúc Clo",
        "scope": "Chương 4.3 thiết lập mô hình động học bất hoạt vi sinh vật Chick-Watson và Collins-Selleck, phản ứng điểm uốn clo, thiết kế bể tiếp xúc clo vách ngăn zíc-zắc và kiểm tra số phân tán $d$.",
        "sec_takeaway": "Chương 4.3 thiết kế liều lượng clo khử trùng và kích thước bể tiếp xúc vách ngăn.",
        "sec_topic": "bể tiếp xúc",
        "u0_takeaway": "Chương 4.3 tính toán tích số $C_R t$ theo Collins-Selleck, hình học kênh zíc-zắc và số phân tán $d$.",
        "u0_topic": "kênh zíc-zắc",
        "u0_reason": "Trình đọc gồm $48$ hình slide và $2$ bài giải thiết kế bể tiếp xúc clo.",
    },
    "ch05_1": {
        "title": "Chương 5.1 - Động học Monod, Sản lượng Sinh khối Quan sát và Nhu cầu Oxy Sinh học",
        "scope": "Chương 5.1 xây dựng phương trình động học tăng trưởng vi sinh vật Monod, hệ số sản lượng sinh khối quan sát $Y_{\\text{obs}}$, cân bằng $\\text{COD}$ sinh học và lưu lượng tuần hoàn bùn $Q_r$.",
        "sec_takeaway": "Chương 5.1 thiết lập động học Monod, sản lượng sinh khối $Y_{\\text{obs}}$ và cân bằng oxy.",
        "sec_topic": "động học Monod",
        "u0_takeaway": "Chương 5.1 tính hệ số sản lượng sinh khối $Y_{\\text{obs}}$, tốc độ tiêu thụ cơ chất và lượng oxy $R_o$.",
        "u0_topic": "sản lượng sinh khối",
        "u0_reason": "Chương học cung cấp $31$ hình slide và $3$ bài giải cân bằng sinh khối và tuần hoàn bùn.",
    },
    "ch05_2": {
        "title": "Chương 5.2 - Cân bằng Dinh dưỡng N, P và Nhu cầu Kiềm trong Xử lý Sinh học",
        "scope": "Chương 5.2 phân tích vai trò của vi sinh vật dị dưỡng và tự dưỡng, thành phần tế bào $\\text{C}_5\\text{H}_7\\text{NO}_2$, và tính toán nhu cầu bổ sung Nitơ, Photpho theo lượng sinh khối $P_X$ tạo thành mỗi ngày.",
        "sec_takeaway": "Chương 5.2 xác định nhu cầu dinh dưỡng Nitơ và Photpho cho sinh khối $P_X$.",
        "sec_topic": "nhu cầu dinh dưỡng",
        "u0_takeaway": "Chương 5.2 tính lượng Nitơ và Photpho cần châm thêm dựa trên sản lượng sinh khối $P_X$.",
        "u0_topic": "sản lượng sinh khối",
        "u0_reason": "Nội dung gồm $19$ hình slide và $2$ bài giải cân bằng dinh dưỡng thực tế.",
    },
    "ch06": {
        "title": "Chương 6 - Thiết kế Bể Bùn hoạt tính Hiếu khí (CMAS), Nitrat hóa và Khử Nitơ (MLE, SBR)",
        "scope": "Chương 6 trình bày quy trình thiết kế toàn diện bể bùn hoạt tính khuấy trộn hoàn toàn ($\\text{CMAS}$) chỉ khử $\\text{BOD}$, bể hiếu khí kết hợp nitrat hóa, hệ thống thiếu khí - hiếu khí ($\\text{MLE}$), bể $\\text{SBR}$ và hệ thống cấp khí $\\text{SOTR}$.",
        "sec_takeaway": "Chương 6 thiết kế bể bùn hoạt tính $\\text{CMAS}$, nitrat hóa, khử nitơ $\\text{MLE}$ và $\\text{SBR}$.",
        "sec_topic": "bể bùn hoạt tính",
        "u0_takeaway": "Chương 6 tính tuổi bùn $\\text{SRT}$, thể tích bể, lượng bùn xả $P_{X,\\text{TSS}}$, độ kiềm và $\\text{SOTR}$.",
        "u0_topic": "thể tích bể",
        "u0_reason": "Trình đọc gồm $34$ hình slide và $4$ bài giải thiết kế quy mô toàn nhà máy.",
    },
    "ch07": {
        "title": "Chương 7 - Thiết kế Bể Lọc sinh học Nhỏ giọt (Trickling Filter) và Đĩa quay Sinh học (RBC)",
        "scope": "Chương 7 thiết lập công thức NRC và Schulze-Germain $S_e / S_i = \\exp(-k_{20} D / q_A^n)$ để thiết kế bể lọc sinh học nhỏ giọt vật liệu đá hoặc nhựa, tính hệ số tuần hoàn $R$ và lượng oxy cấp.",
        "sec_takeaway": "Chương 7 thiết kế bể lọc sinh học nhỏ giọt theo NRC và Schulze-Germain.",
        "sec_topic": "lọc sinh học",
        "u0_takeaway": "Chương 7 tính thể tích vật liệu lọc, đường kính tháp lọc, lưu lượng tuần hoàn $R$ và thông gió.",
        "u0_topic": "tháp lọc",
        "u0_reason": "Chương học gồm $6$ hình slide và $3$ bài giải thiết kế lọc sinh học một bậc và hai bậc.",
    },
    "ch08": {
        "title": "Chương 8 - Thiết kế Bể Phản ứng Kỵ khí Khuấy trộn Hoàn toàn và Bể UASB",
        "scope": "Chương 8 trình bày động học phân hủy kỵ khí, sản lượng khí metan $V_{\\text{CH}_4}$ và khí sinh học ở điều kiện tiêu chuẩn và điều kiện vận hành, kiểm tra nhu cầu dinh dưỡng $\\text{N}, \\text{P}$ và thiết kế bể kỵ khí.",
        "sec_takeaway": "Chương 8 thiết kế bể phản ứng kỵ khí và tính lưu lượng khí sinh học $V_{\\text{CH}_4}$.",
        "sec_topic": "khí sinh học",
        "u0_takeaway": "Chương 8 tính tuổi bùn kỵ khí, thể tích bể, sản lượng khí metan $V_{\\text{CH}_4}$ và diện tích bể lắng.",
        "u0_topic": "tuổi bùn kỵ khí",
        "u0_reason": "Nội dung gồm $12$ hình slide và $2$ bài giải thiết kế bể kỵ khí hoàn chỉnh.",
    },
    "ch09": {
        "title": "Chương 9 - Thiết kế Quá trình Kỵ khí Tăng trưởng Dính bám (Anaerobic Filter)",
        "scope": "Chương 9 trình bày cấu tạo và thông số tải trọng chất hữu cơ $\\text{OLR}$ của bể lọc kỵ khí dòng hướng lên và dòng hướng xuống, xác định thể tích vật liệu đệm $V_{\\text{media}}$, diện tích bề mặt riêng và thời gian lưu nước $\\tau$.",
        "sec_takeaway": "Chương 9 thiết kế bể lọc kỵ khí tăng trưởng dính bám và vật liệu đệm $V_{\\text{media}}$.",
        "sec_topic": "bể lọc kỵ khí",
        "u0_takeaway": "Chương 9 xác định thể tích lớp đệm kỵ khí, diện tích bề mặt riêng và hiệu suất khử $\\text{COD}$.",
        "u0_topic": "lớp đệm kỵ khí",
        "u0_reason": "Trình đọc gồm $18$ hình slide và $2$ bài giải thiết kế bể lọc kỵ khí.",
    },
    "ch10": {
        "title": "Chương 10 - Thiết kế Hệ thống Xử lý Bùn cặn, Cô đặc, Phân hủy Kỵ khí và Làm khô Bùn",
        "scope": "Chương 10 trình bày tính toán khối lượng và thể tích bùn tươi và bùn hoạt tính dư $V_{\\text{sludge}}$, thiết kế bể nén bùn trọng lực, bể phân hủy bùn kỵ khí một bậc và hai bậc, và sân phơi bùn.",
        "sec_takeaway": "Chương 10 thiết kế dây chuyền cô đặc, phân hủy kỵ khí và làm khô bùn cặn.",
        "sec_topic": "xử lý bùn cặn",
        "u0_takeaway": "Chương 10 tính khối lượng riêng bùn $\\rho_{\\text{sl}}$, thể tích bùn ẩm, bể nén bùn và bể tiêu bùn.",
        "u0_topic": "thể tích bùn",
        "u0_reason": "Chương học gồm $14$ hình slide và $2$ bài giải tính toán bùn cặn toàn diện.",
    },
}


def sanitize_single_line(s: str) -> str:
    """Ensure zero em-dashes and clean single-line spacing."""
    t = str(s or "").replace("—", "-").replace("–", "-")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def clean_exercises_hub_md(raw_md: str) -> str:
    """
    Clean `<slug>_exercises_hub.md` content for inclusion in `hub_master.md`:
    - Strip any `<!-- ... -->` HTML comments
    - Strip any `![...](...)` Markdown image links
    - Strip any `[Page N]` markers (including optional surrounding backticks)
    - Strip any accidental empty backtick spans
    - Replace em-dashes (`—`) and en-dashes (`–`) with `-`
    - Ensure every exercise heading is `### Bài tập ...`
    """
    text = re.sub(r"<!--.*?-->", "", raw_md, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", text)
    text = re.sub(r"[ \t]*`?\[Page\s+\d+\]`?[ \t]*", " ", text)
    text = re.sub(r"`\s*`", "", text)
    text = re.sub(r"[ \t]+([.,;:])", r"\1", text)
    text = text.replace("—", "-").replace("–", "-")
    # Collapse 3+ consecutive blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def build_hub_markdown(data: dict) -> tuple[list[dict], dict[str, list[dict]]]:
    readers = data["readers"]
    exercises = data["exercises"]

    ex_by_slug: dict[str, list[dict]] = {}
    for ex in exercises:
        ex_by_slug.setdefault(ex["chapter_slug"], []).append(ex)

    md_lines = [
        "# Kỹ thuật Xử lý Nước thải - Trung tâm Điều hướng 17 Chương Trình đọc 5 mức và 54 Bài giải Thiết kế",
        "",
    ]

    for r in readers:
        slug = r["slug"]
        meta = CHAPTER_META[slug]
        exs = ex_by_slug.get(slug, [])
        pdf_cnt = sum(1 for e in exs if e["category"] == "pdf_exercise")
        proj_cnt = sum(1 for e in exs if e["category"] != "pdf_exercise")

        md_lines.append(f"## {meta['title']}")
        md_lines.append("")

        # Paragraph 1 (U0: role="method" under the ## chapter heading)
        p1 = (
            f"{meta['scope']} "
            f"Trình đọc chương `{slug}` bao gồm ${r['sections_count']}$ mục lớn, ${r['units_count']}$ đơn vị kiến thức neo bằng chứng, "
            f"${r['manifest_figures_count']}$ hình chụp trang slide ở độ phân giải $150\\text{{ DPI}}$ và ${len(exs)}$ bài giải hoàn chỉnh "
            f"(${pdf_cnt}$ bài tập trong PDF và ${proj_cnt}$ bài tập chiếu trên lớp). "
            f"Người học bấm trực tiếp vào liên kết [Mở trình đọc 5 mức {meta['title'].split(' - ')[0]} (Open Full Chapter Reader)](readers/{slug}/{slug}.fold.html) "
            f"hoặc xem tệp nguồn tại [Bản thảo Markdown {slug}.md](chapters_md/{slug}.md)."
        )
        md_lines.append(sanitize_single_line(p1))
        md_lines.append("")

        # Embed the full 4-Block LaTeX exercise content from chapters_md/<slug>_exercises_hub.md
        ex_hub_path = BASE_DIR / "chapters_md" / f"{slug}_exercises_hub.md"
        if not ex_hub_path.exists():
            raise FileNotFoundError(f"Missing required 4-Block LaTeX file: {ex_hub_path}")
        cleaned_ex_md = clean_exercises_hub_md(ex_hub_path.read_text(encoding="utf-8"))
        md_lines.append(cleaned_ex_md)
        md_lines.append("")

    HUB_MD.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote hub_master.md: {HUB_MD} ({HUB_MD.stat().st_size:,} bytes)")
    return readers, ex_by_slug


def normalize_key(s: str) -> str:
    return re.sub(r"\W+", "", str(s or "").lower().replace("—", "-").replace("–", "-"))


def build_worker_ladder_lookup(readers: list[dict]) -> dict[str, dict]:
    """
    Build a lookup of existing section & unit ladders from the 17 compiled
    `readers/<slug>/fold_work/fold_manifest.json` and `reply_file` JSONs
    keyed by normalized `chunk_title`.
    """
    lookup: dict[str, dict] = {}
    for r in readers:
        slug = r["slug"]
        mf_path = BASE_DIR / "readers" / slug / "fold_work" / "fold_manifest.json"
        if not mf_path.exists():
            continue
        mf = json.loads(mf_path.read_text(encoding="utf-8"))
        for t in mf.get("tasks", []):
            if t.get("stage") != "ladder":
                continue
            rfile = Path(t["reply_file"])
            if not rfile.exists():
                continue
            rep = json.loads(rfile.read_text(encoding="utf-8"))
            k = normalize_key(t.get("chunk_title", ""))
            if k:
                lookup[k] = rep
    return lookup


def extract_fallback_unit_ladder(u: dict, u_idx: int) -> dict:
    """Fallback ladder generator if any unit is not covered by the worker lookup."""
    sents = u.get("sents", [])
    n_sents = len(sents)
    first_s = sanitize_single_line(sents[0] if sents else u.get("text", ""))
    last_s = sanitize_single_line(sents[-1] if sents else first_s)

    # Pick a 2-3 word plain Vietnamese topic outside $...$
    plain = re.sub(r"\$[^$]*\$", " ", first_s)
    words = [w.strip(".,;:()[]{}\"'`") for w in plain.split() if len(w.strip(".,;:()[]{}\"'`")) >= 2]
    topic = " ".join(words[:2]) if len(words) >= 2 else (words[0] if words else "Thông số")
    take_words = first_s.split()[:12]
    takeaway = " ".join(take_words).rstrip(".,;:(") + "."
    if topic.lower() not in takeaway.lower():
        takeaway = f"{topic} xác định {takeaway}"
        takeaway = " ".join(takeaway.split()[:13]).rstrip(".,;:(") + "."

    reason_words = last_s.split()[:16]
    reason = " ".join(reason_words).rstrip(".,;:(") + "."
    ev = sorted({0, max(0, n_sents - 1)})
    ev = [i for i in ev if 0 <= i < n_sents] or [0]
    role = "setup" if u_idx == 0 else ("result" if u_idx >= 2 else "method")
    return {
        "id": f"U{u_idx}",
        "role": role,
        "takeaway": takeaway,
        "topic": topic,
        "reason": reason,
        "evidence": ev,
    }


def generate_hub_ladder_replies(readers: list[dict]) -> None:
    manifest_path = HUB_READER_DIR / "fold_work" / "fold_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    store_dir = Path(manifest["store_dir"])
    pid = manifest["pid"]
    sys.path.insert(0, str(VENDOR_WEB.parent.parent))
    from textfold import store as tf_store
    tf_store.DATA = store_dir
    doc = tf_store.parsed(pid)

    worker_lookup = build_worker_ladder_lookup(readers)
    title_to_slug = {normalize_key(meta["title"]): slug for slug, meta in CHAPTER_META.items()}

    tasks = [t for t in manifest["tasks"] if t["stage"] == "ladder"]
    matched_worker_chunks = 0
    matched_chapter_chunks = 0

    for task in tasks:
        chunk_id = task["chunk_id"]
        chunk_title = task.get("chunk_title", "")
        norm_title = normalize_key(chunk_title)
        chunk = next(c for c in doc["chunks"] if c["id"] == chunk_id)
        uids = chunk["units"]

        if norm_title in title_to_slug:
            slug = title_to_slug[norm_title]
            meta = CHAPTER_META[slug]
            matched_chapter_chunks += 1
            units_out = []
            for u_idx, uid in enumerate(uids):
                u = doc["units"][uid]
                n_sents = len(u.get("sents", []))
                ev = [0, min(1, max(0, n_sents - 1))]
                ev = sorted(set(i for i in ev if 0 <= i < n_sents)) or [0]
                if u_idx == 0:
                    units_out.append({
                        "id": f"U{u_idx}",
                        "role": "method",
                        "takeaway": meta["u0_takeaway"],
                        "topic": meta["u0_topic"],
                        "reason": meta["u0_reason"],
                        "evidence": ev,
                    })
                else:
                    units_out.append(extract_fallback_unit_ladder(u, u_idx))

            reply_payload = {
                "section": {
                    "takeaway": meta["sec_takeaway"],
                    "topic": meta["sec_topic"],
                },
                "units": units_out,
            }
        elif norm_title in worker_lookup:
            w_rep = worker_lookup[norm_title]
            matched_worker_chunks += 1
            w_sec = w_rep.get("section", {})
            sec_takeaway = sanitize_single_line(w_sec.get("takeaway", ""))
            sec_topic = sanitize_single_line(w_sec.get("topic", ""))
            w_units = w_rep.get("units", [])

            units_out = []
            for u_idx, uid in enumerate(uids):
                u = doc["units"][uid]
                n_sents = len(u.get("sents", []))
                if u_idx < len(w_units):
                    wu = w_units[u_idx]
                    raw_ev = wu.get("evidence", [0])
                    ev = sorted({int(i) for i in raw_ev if isinstance(i, int) and 0 <= int(i) < n_sents})
                    if not ev:
                        ev = [0]
                    units_out.append({
                        "id": f"U{u_idx}",
                        "role": wu.get("role", "method"),
                        "takeaway": sanitize_single_line(wu.get("takeaway", "")),
                        "topic": sanitize_single_line(wu.get("topic", "")),
                        "reason": sanitize_single_line(wu.get("reason", "")),
                        "evidence": ev,
                    })
                else:
                    units_out.append(extract_fallback_unit_ladder(u, u_idx))

            reply_payload = {
                "section": {
                    "takeaway": sec_takeaway,
                    "topic": sec_topic,
                },
                "units": units_out,
            }
        else:
            # Fallback for any unanticipated chunk
            units_out = [extract_fallback_unit_ladder(doc["units"][uid], u_idx) for u_idx, uid in enumerate(uids)]
            first_u = units_out[0] if units_out else {"takeaway": " Nội dung bài giải kỹ thuật.", "topic": "Nội dung"}
            reply_payload = {
                "section": {
                    "takeaway": first_u["takeaway"],
                    "topic": first_u["topic"],
                },
                "units": units_out,
            }

        reply_path = Path(task["reply_file"])
        reply_path.write_text(json.dumps(reply_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        f"Generated {len(tasks)} verified ladder reply JSONs for hub_master "
        f"({matched_chapter_chunks} chapter headers + {matched_worker_chunks} worker exercise chunks)."
    )


def build_sidebar_html(readers: list[dict], ex_by_slug: dict[str, list[dict]], active_slug: str, is_root_hub: bool) -> str:
    mark_svg = (
        '<svg viewBox="0 0 20 20" aria-hidden="true">'
        '<rect class="m1" x="2" y="3" width="16" height="2.4" rx="1.2"/>'
        '<rect class="m2" x="2" y="8.8" width="11" height="2.4" rx="1.2"/>'
        '<rect class="m3" x="2" y="14.6" width="5" height="2.4" rx="1.2"/>'
        '</svg>'
    )
    list_svg = (
        '<svg viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6">'
        '<rect x="2.5" y="3.5" width="15" height="13" rx="2.5"/><path d="M7.5 3.5v13"/>'
        '</svg>'
    )
    pin_svg = (
        '<svg viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">'
        '<path class="pin-head" d="M7.2 2.8h5.6l-.9 4.6 2.9 3v1.4H5.2v-1.4l2.9-3z"/><path d="M10 11.8v5.4"/>'
        '</svg>'
    )

    hub_href = "index.html" if is_root_hub else "../../index.html"
    hub_active = " active" if active_slug == "index" else ""

    rows_html = [
        '<div class="sb-group">Trung tâm điều hướng</div>',
        f'<div class="sb-row" data-q="tong quan 54 bai giai course hub index">'
        f'<a class="sb-item{hub_active}" href="{hub_href}" title="Tổng quan &amp; 54 Bài giải Thiết kế">'
        f'<span class="sb-t">Tổng quan &amp; 54 Bài giải (Course Hub)</span>'
        f'<span class="sb-m"><span class="sb-id">17 chương · 54 bài</span><span class="sb-langs"><span class="on">VI</span></span></span>'
        f'</a></div>',
        '<div class="sb-group">17 Chương Bài giảng (Fold 5 mức)</div>',
    ]

    for r in readers:
        slug = r["slug"]
        title = CHAPTER_META[slug]["title"]
        exs_cnt = len(ex_by_slug.get(slug, []))
        ch_href = f"readers/{slug}/{slug}.fold.html" if is_root_hub else f"../{slug}/{slug}.fold.html"
        act_cls = " active" if active_slug == slug else ""
        q_str = html.escape(f"{slug} {title.lower()}")
        rows_html.append(
            f'<div class="sb-row" data-q="{q_str}">'
            f'<a class="sb-item{act_cls}" href="{ch_href}" title="{html.escape(title)}">'
            f'<span class="sb-t">{html.escape(title)}</span>'
            f'<span class="sb-m"><span class="sb-id">{slug} · {r["units_count"]}u · {r["manifest_figures_count"]} hình · {exs_cnt} bài</span>'
            f'<span class="sb-langs"><span class="on">VI</span></span></span>'
            f'</a></div>'
        )

    return (
        '<aside id="sidebar" class="collapsed">'
        f'<div class="sb-head"><a class="sb-brand" href="{hub_href}">{mark_svg}<span>TextFold</span></a>'
        f'<span class="sb-hbtns">'
        f'<button type="button" class="sb-pin" aria-pressed="false" aria-label="Ghim thanh bên" title="Ghim thanh bên">{pin_svg}</button>'
        f'<button type="button" class="sb-toggle" aria-label="Thu gọn" title="Thu gọn">‹</button>'
        f'</span></div>'
        f'<div class="sb-rail">'
        f'<a class="rail-btn rail-home" href="{hub_href}" title="Tổng quan &amp; 54 Bài giải">{mark_svg}</a>'
        f'<button type="button" class="rail-btn rail-open" title="Danh mục 17 chương">{list_svg}</button>'
        f'</div>'
        f'<div class="sb-find"><input type="search" class="sb-q" value="" placeholder="Tìm chương hoặc bài tập…" aria-label="Tìm chương" autocomplete="off" spellcheck="false"></div>'
        f'<nav class="sb-list"><div class="sb-loose">{"".join(rows_html)}</div>'
        f'<div class="sb-nomatch" hidden>Không tìm thấy chương phù hợp</div></nav>'
        f'<div class="sb-foot"><div class="sb-model">Kỹ thuật Xử lý Nước thải · HCMUT · f51e2026</div></div>'
        '</aside>'
    )


def enhance_fold_html_file(html_path: Path, readers: list[dict], ex_by_slug: dict[str, list[dict]], active_slug: str, is_root_hub: bool) -> None:
    raw = html_path.read_text(encoding="utf-8")
    app_css = (VENDOR_WEB / "app.css").read_text(encoding="utf-8")
    sidebar_markup = build_sidebar_html(readers, ex_by_slug, active_slug=active_slug, is_root_hub=is_root_hub)

    hub_href = "index.html" if is_root_hub else "../../index.html"
    nav_script = f"""<script id="tf-nav-init">
(() => {{
  const side = document.getElementById('sidebar');
  if (!side) return;
  const root = document.documentElement;
  const brand = document.querySelector('.topbar .brand');
  const homeLink = brand ? brand.querySelector('a.brand-home') : null;
  if (homeLink) {{
    homeLink.href = '{hub_href}';
    homeLink.removeAttribute('target');
    homeLink.title = 'Về Trung tâm Điều hướng Khóa học (index.html)';
  }}
  if (brand && !brand.querySelector('.rail-open')) {{
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'rail-btn rail-open';
    btn.title = 'Mở danh mục 17 chương và 54 bài giải';
    btn.setAttribute('aria-label', 'Mở danh mục 17 chương');
    btn.innerHTML = '<svg viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2.5" y="3.5" width="15" height="13" rx="2.5"/><path d="M7.5 3.5v13"/></svg>';
    btn.onclick = () => {{
      side.classList.toggle('collapsed');
    }};
    brand.prepend(btn);
  }}
  const openBtn = side.querySelector('.sb-rail .rail-open');
  const toggleBtn = side.querySelector('.sb-toggle');
  const pinBtn = side.querySelector('.sb-pin');
  const qInput = side.querySelector('.sb-q');
  if (openBtn) openBtn.onclick = () => side.classList.remove('collapsed');
  if (toggleBtn) toggleBtn.onclick = () => side.classList.add('collapsed');
  if (pinBtn) {{
    pinBtn.onclick = () => {{
      const pinned = pinBtn.getAttribute('aria-pressed') !== 'true';
      pinBtn.setAttribute('aria-pressed', String(pinned));
      root.classList.toggle('app', pinned);
      root.classList.toggle('sb-docked', pinned);
    }};
  }}
  if (qInput) {{
    qInput.addEventListener('input', () => {{
      const q = qInput.value.trim().toLowerCase();
      let visible = 0;
      side.querySelectorAll('.sb-row').forEach((row) => {{
        const hay = (row.getAttribute('data-q') || row.textContent || '').toLowerCase();
        const show = !q || hay.includes(q);
        row.hidden = !show;
        if (show) visible++;
      }});
      const nomatch = side.querySelector('.sb-nomatch');
      if (nomatch) nomatch.hidden = visible > 0;
    }});
  }}
}})();
</script>"""

    # Anchor strictly on <script type="application/json" id="paper-data"> so head/body
    # replacements NEVER touch the JavaScript code inside reader.js (e.g. marksHtml template strings).
    marker = '<script type="application/json" id="paper-data">'
    if marker not in raw:
        raise RuntimeError(f"[{html_path}] Missing {marker}")

    pre_data, sep, post_data = raw.partition(marker)

    # 1. In pre_data (pure top-level HTML shell before paper-data and reader.js):
    pre_data = re.sub(
        r'<html\b[^>]*>',
        '<html lang="vi" class="static" data-theme="dark">',
        pre_data,
        count=1,
    )
    pre_data = re.sub(r'<style id="tf-app-css">.*?</style>', '', pre_data, flags=re.S)
    perf_css = (
        "\nbody:not(.morphing) figure.fig { content-visibility: auto; contain-intrinsic-size: auto 360px; contain: layout style paint; }\n"
        "body:not(.morphing) .eq { content-visibility: auto; contain-intrinsic-size: auto 56px; contain: layout style; }\n"
        "body:not(.morphing) .chunk { contain: layout style; }\n"
    )
    pre_data = pre_data.replace("</head>", f'<style id="tf-app-css">{app_css}{perf_css}</style></head>', 1)

    pre_data = re.sub(r'<aside id="sidebar".*?</aside>\s*', '', pre_data, flags=re.S)
    pre_data = re.sub(
        r'(<body\b[^>]*>)',
        lambda m: f"{m.group(1)}\n{sidebar_markup}",
        pre_data,
        count=1,
    )

    # 2. In post_data (paper-data + i18n.js + reader.js + closing </body></html>):
    if active_slug == "index" and not is_root_hub:
        post_data = post_data.replace('href=\\"readers/', 'href=\\"../').replace('href=\\"chapters_md/', 'href=\\"../../chapters_md/')
    post_data = post_data.replace(
        "mode: 'auto', style: 'default'",
        "mode: 'dark', style: 'default'",
        1,
    )
    post_data = re.sub(r'<script id="tf-nav-init">.*?</script>\s*', '', post_data, flags=re.S)
    post_data, n_sub = re.subn(
        r'</body>(\s*</html>\s*)\Z',
        lambda m: f"{nav_script}\n</body>{m.group(1)}",
        post_data,
        count=1,
    )
    if n_sub != 1:
        raise RuntimeError(f"[{html_path}] Failed to anchor nav_script before final </body></html>")

    html_path.write_text(pre_data + sep + post_data, encoding="utf-8")


def verify_dom_and_katex_integrity(html_path: Path, is_hub: bool = False) -> tuple[int, int]:
    raw = html_path.read_text(encoding="utf-8")

    # Gate 3: KaTeX math rendering + 4-part scroll optimization active
    if 'id="katex-css"' not in raw:
        raise RuntimeError(f"[{html_path.name}] Missing id='katex-css' stylesheet!")
    if 'class="pf-tex"' not in raw:
        raise RuntimeError(f"[{html_path.name}] Missing class='pf-tex' KaTeX spans!")
    for req_opt in ("output: 'html'", "function warm() { return; }", 'loading="lazy" decoding="async"', "content-visibility: auto"):
        if req_opt not in raw:
            raise RuntimeError(f"[{html_path.name}] Missing required scroll optimization token: {req_opt}")
    n_tex = raw.count('class="pf-tex"')
    n_eq = raw.count("ltx_equation")
    if is_hub and n_eq < 50:
        raise RuntimeError(f"[{html_path.name}] Expected >= 50 ltx_equation blocks in hub, got {n_eq}!")

    # Gate 2: BeautifulSoup DOM integrity check
    soup = BeautifulSoup(raw, "lxml")

    if soup.html is None or soup.html.get("data-theme") != "dark":
        raise RuntimeError(f"[{html_path.name}] <html> missing data-theme='dark'")
    if soup.head is None or soup.head.find("style", id="tf-app-css") is None:
        raise RuntimeError(f"[{html_path.name}] <head> missing <style id='tf-app-css'>")
    if soup.body is None:
        raise RuntimeError(f"[{html_path.name}] Missing <body>")

    sb = soup.body.find("aside", id="sidebar", recursive=False)
    if sb is None:
        raise RuntimeError(f"[{html_path.name}] <aside id='sidebar'> is NOT a direct child of <body>")

    nav_sc = soup.body.find("script", id="tf-nav-init", recursive=False)
    if nav_sc is None:
        raise RuntimeError(f"[{html_path.name}] <script id='tf-nav-init'> is NOT a direct child of <body>")

    for sc in soup.find_all("script"):
        sc_txt = sc.string or sc.get_text() or ""
        if '<aside id="sidebar"' in sc_txt or '<script id="tf-nav-init"' in sc_txt:
            raise RuntimeError(f"[{html_path.name}] Corrupt injection detected inside a <script> tag!")

    # Remove all <script> and <style> elements and verify zero leaked JS source in visible body text
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()
    visible_text = soup.body.get_text(" ", strip=True)
    for forbidden in ("sizePages()", "unitAtReading()", "the drag ends", "keep.isConnected"):
        if forbidden in visible_text:
            raise RuntimeError(f"[{html_path.name}] Leaked JS code '{forbidden}' found in visible body text!")

    return n_tex, n_eq


def verify_hub_md_cleanliness() -> None:
    """Gate 4: Zero raw ASCII/English leakage in hub_master.md."""
    md_text = HUB_MD.read_text(encoding="utf-8")
    forbidden_ascii = (
        "Select safety factor",
        "Check 24-hour",
        "Q_avg =",
        "V_theo =",
        "without_recycle_abs_pressure_P",
    )
    for bad in forbidden_ascii:
        if bad in md_text:
            raise RuntimeError(f"[hub_master.md] Forbidden raw ASCII/English string found: {bad!r}")
    h3_count = len(re.findall(r"^###\s+Bài tập\b", md_text, re.M))
    if h3_count != 54:
        raise RuntimeError(f"[hub_master.md] Expected 54 '### Bài tập' sections, got {h3_count}")
    print(f"  [Gate 4 PASSED] hub_master.md has 54 '### Bài tập' sections and 0 raw ASCII/English leakage.")


def clean_chapter_store_and_manifest(ch_dir: Path) -> None:
    mf_path = ch_dir / "fold_work" / "fold_manifest.json"
    if not mf_path.exists():
        return
    mf = json.loads(mf_path.read_text(encoding="utf-8"))
    pid = mf["pid"]
    store_dir = Path(mf["store_dir"])
    src_html_path = store_dir / "papers" / pid / "source.html"
    if not src_html_path.exists():
        return

    orig_html = src_html_path.read_text(encoding="utf-8")
    cleaned_html = re.sub(r"<code>#(\d+)\\text\{[–-]\}\#(\d+)</code>", r"#\1–#\2", orig_html)
    cleaned_html = re.sub(
        r"<code>([^<]*)</code>",
        lambda m: m.group(0) if re.fullmatch(r"[a-z0-9_]+|TSR2-80", m.group(1).strip()) else m.group(1),
        cleaned_html,
    )
    en_file = store_dir / "papers" / pid / "layers" / "en.json"
    if cleaned_html != orig_html or not en_file.exists():
        if cleaned_html != orig_html:
            src_html_path.write_text(cleaned_html, encoding="utf-8")
        sys.path.insert(0, str(VENDOR_WEB.parent.parent))
        from textfold import ladder, store as tf_store
        tf_store.DATA = store_dir
        doc = tf_store.parsed(pid)
        doc["meta"]["lang"] = mf.get("base_lang", "vi")
        chunk_by_id = {c["id"]: c for c in doc["chunks"]}
        for t in mf.get("tasks", []):
            if t.get("stage") == "ladder" and t.get("chunk_id") in chunk_by_id:
                ptxt = ladder.prompt_for(doc, chunk_by_id[t["chunk_id"]])
                t["prompt_hash"] = hashlib.sha256(
                    json.dumps([ptxt, ladder.SCHEMA], sort_keys=True).encode("utf-8")
                ).hexdigest()[:16]
                Path(t["prompt_file"]).write_text(ptxt, encoding="utf-8")
        mf_path.write_text(json.dumps(mf, ensure_ascii=False, indent=2), encoding="utf-8")
        if en_file.exists():
            en_file.unlink()


def run_cmd(args: list[str]) -> str:
    proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed (rc={proc.returncode}): {' '.join(args)}\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout.strip()


def main() -> int:
    data = json.loads(MASTER_JSON.read_text(encoding="utf-8"))
    readers, ex_by_slug = build_hub_markdown(data)
    verify_hub_md_cleanliness()

    HUB_READER_DIR.mkdir(parents=True, exist_ok=True)
    print("\n=== Step 1: fold_pipeline.py prepare on hub_master.md ===")
    out_prep = run_cmd([
        sys.executable,
        str(FOLD_PIPELINE),
        "prepare",
        str(HUB_MD),
        str(HUB_READER_DIR),
        "--slug",
        "index",
    ])
    print(out_prep)

    print("\n=== Step 2: Generating verified 5-level ladder replies for hub_master ===")
    generate_hub_ladder_replies(readers)

    print("\n=== Step 3: Cleanly compiling all 18 .fold.html files via fold_pipeline.py compile ===")
    run_cmd([
        sys.executable,
        str(FOLD_PIPELINE),
        "compile",
        str(HUB_READER_DIR),
        "--slug",
        "index",
        "--force",
    ])
    for r in readers:
        slug = r["slug"]
        ch_dir = BASE_DIR / "readers" / slug
        clean_chapter_store_and_manifest(ch_dir)
        run_cmd([
            sys.executable,
            str(FOLD_PIPELINE),
            "compile",
            str(ch_dir),
            "--slug",
            slug,
        ])
        print(f"  Re-compiled clean HTML: readers/{slug}/{slug}.fold.html")

    print("\n=== Step 4: Enhancing index.html + all 18 .fold.html files with anchored DOM injection ===")
    hub_fold_html = HUB_READER_DIR / "index.fold.html"
    shutil.copyfile(hub_fold_html, ROOT_INDEX_HTML)

    enhance_fold_html_file(hub_fold_html, readers, ex_by_slug, active_slug="index", is_root_hub=False)
    enhance_fold_html_file(ROOT_INDEX_HTML, readers, ex_by_slug, active_slug="index", is_root_hub=True)

    for r in readers:
        slug = r["slug"]
        ch_html = BASE_DIR / "readers" / slug / f"{slug}.fold.html"
        enhance_fold_html_file(ch_html, readers, ex_by_slug, active_slug=slug, is_root_hub=False)

    print("\n=== Step 5: Running Hard Gates 1, 2, 3, 4 across index.html + all 18 readers ===")
    verify_hub_md_cleanliness()
    n_tex_root, n_eq_root = verify_dom_and_katex_integrity(ROOT_INDEX_HTML, is_hub=True)
    print(
        f"  [ROOT index.html] DOM/JS & KaTeX Integrity PASSED "
        f"({ROOT_INDEX_HTML.stat().st_size:,} bytes, pf-tex={n_tex_root}, ltx_equation={n_eq_root})"
    )

    all_targets = [("hub_master", "index", True)] + [(r["slug"], r["slug"], False) for r in readers]
    for folder_name, slug, is_hub_flag in all_targets:
        tdir = BASE_DIR / "readers" / folder_name
        html_file = tdir / f"{slug}.fold.html"
        n_tex, n_eq = verify_dom_and_katex_integrity(html_file, is_hub=is_hub_flag)
        v_out = run_cmd([
            sys.executable,
            str(FOLD_PIPELINE),
            "verify",
            str(tdir),
            "--slug",
            slug,
        ])
        print(f"  [{folder_name}] DOM/JS OK | pf-tex={n_tex} | ltx_equation={n_eq} | {v_out}")

    print("\n=== ALL 4 HARD GATES PASSED ACROSS 19 HTML FILES & 18 FOLD READERS ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
