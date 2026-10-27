import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Set standard margins (1 inch)
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Helper function to style headings
def add_custom_heading(text, level, color=RGBColor(7, 23, 41)):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    for run in h.runs:
        run.font.name = 'Arial'
        run.font.color.rgb = color
    return h

# Set cell background color
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

# Title & Header
title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_uni = title_p.add_run("TRƯỜNG ĐẠI HỌC VĂN HIẾN\nKHOA KINH TẾ - QUẢN TRỊ / MARKETING\n\n")
r_uni.font.name = 'Arial'
r_uni.font.size = Pt(12)
r_uni.font.bold = True
r_uni.font.color.rgb = RGBColor(14, 43, 77)

r_title = title_p.add_run("BÁO CÁO KIỂM TRA GIỮA KỲ\n")
r_title.font.name = 'Arial'
r_title.font.size = Pt(18)
r_title.font.bold = True
r_title.font.color.rgb = RGBColor(197, 155, 39)

r_sub = title_p.add_run("ĐỀ TÀI: XÂY DỰNG CHIẾN DỊCH MARKETING ONLINE & THIẾT KẾ LANDING PAGE QUẢNG BÁ TUYỂN SINH ĐẠI HỌC VĂN HIẾN (VHU)\n(Phong cách thiết kế chuẩn Editorial Luxury dựa trên cấu trúc website TNG Trading)\n")
r_sub.font.name = 'Arial'
r_sub.font.size = Pt(13)
r_sub.font.bold = True
r_sub.font.color.rgb = RGBColor(7, 23, 41)

# Student Info Box
info_table = doc.add_table(rows=5, cols=2)
info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
info_data = [
    ("Môn học:", "Marketing Trực Tuyến (Online Marketing)"),
    ("Bài kiểm tra:", "Kiểm tra giữa kỳ - Sáng tạo nội dung & Xây dựng Landing Page"),
    ("Đối tượng thụ hưởng:", "Phụ huynh & Học sinh lớp 12 chuẩn bị chọn trường Đại học"),
    ("Link sản phẩm thực tế:", "http://localhost:8080/ (Chạy trực tiếp từ mã nguồn D:\\VHU)"),
    ("Thời gian hoàn thành:", "Tháng 10/2026")
]
for i, (label, val) in enumerate(info_data):
    row = info_table.rows[i]
    cell_lbl, cell_val = row.cells[0], row.cells[1]
    cell_lbl.width = Inches(2.2)
    cell_val.width = Inches(4.3)
    
    p0 = cell_lbl.paragraphs[0]
    r0 = p0.add_run(label)
    r0.font.bold = True
    r0.font.size = Pt(10)
    
    p1 = cell_val.paragraphs[0]
    r1 = p1.add_run(val)
    r1.font.size = Pt(10)
    if "http" in val:
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(0, 77, 193)

doc.add_paragraph().paragraph_format.space_after = Pt(12)

# --- PHẦN 1 ---
add_custom_heading("1. Ý TƯỞNG CHỦ ĐỀ CHIẾN DỊCH (BIG IDEA & CONCEPT)", level=1, color=RGBColor(14, 43, 77))

doc.add_paragraph(
    "1.1. Tên chủ đề chiến dịch (Campaign Theme):\n"
    "\"KHỞI ĐẦU THÀNH NHÂN – KIẾN TẠO TƯƠNG LAI\"\n"
    "(Developing Character Before Career — Shaping Tomorrow)"
)

doc.add_paragraph(
    "1.2. Bối cảnh & Cảm hứng sáng tạo:\n"
    "Chiến dịch marketing online được thiết kế theo đơn đặt hàng chiến lược nhằm định vị lại hình ảnh của Trường Đại học Văn Hiến (VHU) trong tâm trí học sinh THPT và các bậc phụ huynh trước mùa tuyển sinh 2026 - 2027. "
    "Lấy cảm hứng từ chuẩn mực thiết kế tối giản, tinh tế, sang trọng của website TNG Trading (Seoul, Hàn Quốc) kết hợp cùng hệ giá trị cốt lõi 27 năm của Đại học Văn Hiến: \"Thành nhân trước thành danh\"."
)

doc.add_paragraph(
    "1.3. Thông điệp cốt lõi (Core Message):\n"
    "Đại học không chỉ là nơi học nghề để kiếm sống, mà là nơi rèn luyện nhân cách, bản lĩnh và trang bị năng lực thực chiến toàn diện. "
    "Với sự bảo trợ của Tập đoàn Hùng Hậu (HungHau Holdings), VHU đưa ra cam kết vàng: 100% sinh viên được giới thiệu việc làm sau tốt nghiệp, thực tập có lương từ năm 2, và cam kết KHÔNG TĂNG HỌC PHÍ suốt toàn bộ 4 năm học."
)

# --- PHẦN 2 ---
add_custom_heading("2. PHÂN TÍCH KHÁCH HÀNG MỤC TIÊU & INSIGHT", level=1, color=RGBColor(14, 43, 77))

doc.add_paragraph(
    "Chiến dịch nhắm đến 2 nhóm đối tượng khách hàng mục tiêu với những nỗi lo (Pain Points) và mong muốn (Needs) rõ rệt:"
)

table_target = doc.add_table(rows=4, cols=3)
table_target.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Nhóm khách hàng", "Nỗi trăn trở (Pain points)", "Giải pháp Landing Page đáp ứng"]
for col_idx, h_text in enumerate(headers):
    cell = table_target.rows[0].cells[col_idx]
    set_cell_background(cell, "0E2B4D")
    p = cell.paragraphs[0]
    r = p.add_run(h_text)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    r.font.size = Pt(10)

target_rows = [
    ("Phụ huynh học sinh\n(Người chi trả & Định hướng)", 
     "- Lo sợ học phí tăng bất ngờ theo từng năm.\n- Lo con ra trường thất nghiệp, bằng cấp không thực tế.\n- Lo môi trường đại học xa nhà thiếu an toàn.", 
     "✓ Cam kết bằng văn bản KHÔNG TĂNG HỌC PHÍ 4 năm.\n✓ Cam kết 100% giới thiệu việc làm tại 500+ doanh nghiệp.\n✓ Quần thể HungHau Campus 60.000m² an ninh 24/7."),
    
    ("Học sinh lớp 12\n(Người trực tiếp thụ hưởng)", 
     "- Áp lực thi cử, sợ điểm thi không đủ đỗ trường lớn.\n- Mông lung chưa biết ngành nào hot, thu nhập cao.\n- Muốn được học tập trải nghiệm năng động, hiện đại.", 
     "✓ Công cụ tính điểm học bạ online biết kết quả ngay.\n✓ Danh mục 44 ngành rõ lộ trình nghề nghiệp và lương.\n✓ Sân khấu Beethoven, Lab AI, cơ hội du học trao đổi."),
    
    ("Gia đình có hoàn cảnh khó khăn", 
     "- Thiếu kinh phí đóng học kỳ đầu tiên.\n- Nguy cơ đứt gãy việc học vì gánh nặng tài chính.", 
     "✓ Tài trợ 50% học phí Học kỳ 1 ngay khi nhập học.\n✓ Quỹ Trái Tim Hùng Hậu cho vay 0% lãi suất.\n✓ Quỹ học bổng thường niên 50 tỷ đồng.")
]

for row_idx, data_tuple in enumerate(target_rows, start=1):
    for col_idx, text_val in enumerate(data_tuple):
        cell = table_target.rows[row_idx].cells[col_idx]
        p = cell.paragraphs[0]
        r = p.add_run(text_val)
        r.font.size = Pt(9.5)

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# --- PHẦN 3 ---
add_custom_heading("3. CHIẾN LƯỢC SÁNG TẠO NỘI DUNG (6 CAM KẾT VÀNG VHU)", level=1, color=RGBColor(14, 43, 77))

commitments = [
    ("Cam kết 01: Cam kết việc làm 100% sau tốt nghiệp", "Ký kết hợp đồng giới thiệu việc làm với hơn 500 doanh nghiệp trong và ngoài nước thuộc hệ sinh thái HungHau Holdings."),
    ("Cam kết 02: Thực tập hưởng lương từ năm thứ 2", "Sinh viên được gửi đến làm việc thực tế, cọ xát kỹ năng chuyên môn và có thu nhập ngay từ giai đoạn học đại học."),
    ("Cam kết 03: KHÔNG TĂNG HỌC PHÍ suốt toàn khóa học", "Cố định mức học phí trên mỗi tín chỉ trong toàn bộ 4 năm đào tạo (136 - 150 tín chỉ), minh bạch và không phát sinh phụ phí ẩn."),
    ("Cam kết 04: Đồng hành tài chính & Vay vốn 0% lãi suất", "Quỹ Trái Tim Hùng Hậu hỗ trợ vay học phí không lãi suất, giãn kỳ đóng giúp mọi học sinh đều có cơ hội vào đại học."),
    ("Cam kết 05: Một giảng đường - Nhiều môi trường trải nghiệm", "Đào tạo tích hợp học kỳ doanh nghiệp (Co-op), workshop cùng chuyên gia đầu ngành, tham quan thực tế và các dự án xã hội."),
    ("Cam kết 06: Học bổng phát triển nguồn nhân lực địa phương", "Ngân sách học bổng lên đến 50 tỷ đồng: giảm 50% học phí HK1, học bổng Chắp cánh ước mơ, học bổng Thủ khoa, học bổng Tài năng.")
]

for title, desc in commitments:
    p = doc.add_paragraph()
    r_t = p.add_run(f"• {title}: ")
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(14, 43, 77)
    r_d = p.add_run(desc)
    r_d.font.size = Pt(10.5)

# --- PHẦN 4 ---
add_custom_heading("4. THIẾT KẾ BỐ CỤC & TRẢI NGHIỆM LANDING PAGE DỰA TRÊN TNG TRADING", level=1, color=RGBColor(14, 43, 77))

doc.add_paragraph(
    "Landing page được thiết kế theo đúng quy chuẩn Editorial Luxury & Technical Precision từ website TNG Trading (Hàn Quốc), kế thừa các đặc trưng mỹ thuật cao cấp:\n"
    "• Typography 3 tầng chuẩn mực:\n"
    "  - Serif Headline: Playfair Display (chuẩn nhận diện sang trọng, học thuật) (tạo cảm giác học thuật, uy tín, danh giá).\n"
    "  - Sans-Serif Body & Numerals: Plus Jakarta Sans & Inter (chuẩn DuAn_ThueNha, chữ số sắc nét, rõ ràng) (trong trẻo, hiện đại, dễ đọc trên mọi thiết bị).\n"
    "  - Numerals & Badges: Plus Jakarta Sans Tabular Numbers (chữ số đều đặn, không bị nhảy dòng hay khó đọc) (nhãn kỹ thuật, mã ngành, số liệu chuẩn xác).\n"
    "• Bảng màu (Color Scheme): Deep Royal Navy (#071729) làm chủ đạo thể hiện sự vững chãi, kết hợp cùng Warm Champagne Gold (#C59B27) sang trọng và nền giấy ngà Paper (#FBFBFC).\n"
    "• Hiệu ứng điện ảnh (Cinematic Visuals): Lớp phủ Film Grain mịn màng, hiệu ứng làm mờ kính thủy tinh (Glassmorphism backdrop-blur) ở thanh điều hướng, và khung hình duotone tinh tế.\n"
    "• Bố cục các phân đoạn (Sections Flow):\n"
    "  1. Hero Section: Display Typography, video/ảnh nền khuôn viên, nút kêu gọi kép, 4 chỉ số vàng.\n"
    "  2. Di sản & Triết lý: Đoạn văn báo chí đối xứng cùng hình ảnh khuôn viên duotone.\n"
    "  3. 6 Cam Kết Vàng: Khung lưới 2 cột đánh số thứ tự từ 01 đến 06 đặc trưng phong cách TNG.\n"
    "  4. Spotlight Ngành Mũi Nhọn: Bảng chọn khoa tương tác (giống mẫu trưng bày sản phẩm Glowline của TNG).\n"
    "  5. Thư viện 44 Ngành Đào Tạo: Bộ lọc danh mục tức thì, thanh tìm kiếm thông minh, thẻ ngành tích hợp tính năng xem chi tiết tổ hợp môn và số tín chỉ.\n"
    "  6. Công Cụ Tính Điểm Học Bạ & Học Phí: Tương tác tính điểm tức thời, hiển thị học phí sau ưu đãi 50%.\n"
    "  7. 5 Phương Thức Tuyển Sinh: Hướng dẫn chi tiết cách thức nộp hồ sơ.\n"
    "  8. Hệ Thống Campus 5 Sao: Thư viện ảnh HungHau Campus, Beethoven Hall, AI Lab.\n"
    "  9. Landing Page Form Xét Tuyển: Biểu mẫu đăng ký trực tuyến tối ưu tỷ lệ chuyển đổi, cấp mã hồ sơ tự động.\n"
    "  10. Footer 5 Cột: Địa chỉ 5 cơ sở, số hotline miễn cước 1800 1568, mạng xã hội."
)

# --- PHẦN 5 ---
add_custom_heading("5. HÌNH ẢNH SẢN PHẨM & CÁC TÍNH NĂNG NỔI BẬT", level=1, color=RGBColor(14, 43, 77))

# Insert available images into docx if exists
imgs_to_embed = [
    ("assets/docx_imgs/i1.380881c84974e0cb603b.jpg", "Hình 1: Banner chính & Khuôn viên sinh thái HungHau Campus (Trụ sở chính VHU)"),
    ("assets/docx_imgs/i2.89ee825551a01d8e5ce6.jpg", "Hình 2: Giảng đường hiện đại và không gian học tập trải nghiệm của sinh viên"),
    ("assets/docx_imgs/i40.8835ce749c623e075559.jpg", "Hình 3: Nhà hát - Hội trường Beethoven 1.000 chỗ ngồi phục vụ các sự kiện nghệ thuật"),
    ("assets/docx_imgs/i41.99b78c9c6cf4899ff0b6.jpg", "Hình 4: Hệ thống giảng đường thông minh Smart Classroom và phòng thực hành công nghệ cao")
]

for img_path, caption in imgs_to_embed:
    if os.path.exists(img_path):
        try:
            doc.add_picture(img_path, width=Inches(6.0))
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_cap = p_cap.add_run(caption)
            r_cap.font.italic = True
            r_cap.font.size = Pt(9.5)
            r_cap.font.color.rgb = RGBColor(100, 100, 100)
            doc.add_paragraph().paragraph_format.space_after = Pt(6)
        except Exception as e:
            print(f"Could not embed {img_path}: {e}")

# --- PHẦN 6 ---
add_custom_heading("6. ĐƯỜNG LINK SẢN PHẨM & HƯỚNG DẪN TRUY CẬP", level=1, color=RGBColor(14, 43, 77))

p_link = doc.add_paragraph()
r_link_lbl = p_link.add_run("• Đường dẫn truy cập trực tiếp Website (Local Server): ")
r_link_lbl.font.bold = True
r_link_val = p_link.add_run("http://localhost:8080/\n")
r_link_val.font.bold = True
r_link_val.font.color.rgb = RGBColor(0, 77, 193)

p_link.add_run("• Thư mục mã nguồn dự án: ")
r_code_dir = p_link.add_run("D:\\VHU\n")
r_code_dir.font.name = 'Consolas'

p_link.add_run(
    "• Cấu trúc tệp tin chính:\n"
    "  - index.html: Mã nguồn giao diện Landing Page chuẩn HTML5 ngữ nghĩa.\n"
    "  - styles.css: Hệ thống thiết kế Design Tokens, Typography và Layout kế thừa TNG Trading.\n"
    "  - app.js: Bộ xử lý tương tác động (Lọc 44 ngành, tính điểm học bạ, xử lý form xét tuyển, modal popup).\n"
    "  - majors-data.js: Cơ sở dữ liệu 44 ngành trích xuất trực tiếp từ API Cổng tuyển sinh Đại học Văn Hiến.\n"
    "  - assets/images/: Thư mục tài nguyên logo, ảnh chụp giảng đường, hội trường, phòng học thông minh."
)

# Output docx
output_file = 'BAOCAO_KIEMTRA_GIUAKY_VHU.docx'
doc.save(output_file)
print(f"Successfully generated {output_file}")
