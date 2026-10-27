# Cổng Tuyển Sinh Đại Học Văn Hiến (VHU) - Landing Page 2026

Landing Page tuyển sinh chính thức dành cho **Trường Đại học Văn Hiến (VHU)** niên khóa 2026 - 2027.  
Dự án được thiết kế theo phong cách **Editorial Luxury & Technical Precision** kế thừa kiến trúc và trải nghiệm của website **TNG Trading (Seoul, KR)** và hệ thống typography của **DuAn_ThueNha** (Playfair Display + Plus Jakarta Sans & Inter).

---

## 🌟 Tính Năng Nổi Bật

1. **Bố Cục Editorial Sang Trọng**:
   - Thanh điều hướng kính mờ (Glassmorphism Sticky Blur Header).
   - Hero Section điện ảnh với scrim đa lớp, loại bỏ hiện tượng đè chữ lên hình nền.
   - Thống kê 4 chỉ số vàng: *100% Cam kết việc làm, 0% Không tăng học phí, 50% Hỗ trợ HK1, 60.000m² Campus*.
2. **6 Cam Kết Vàng VHU**:
   - Trình bày dạng lưới 2 cột đánh số thứ tự `01` - `06` chuẩn TNG Trading.
3. **Thư Viện 44 Ngành Đào Tạo Chính Quy**:
   - Dữ liệu trích xuất chính thức từ Cổng tuyển sinh trường VHU (`/api/tuition`).
   - Bộ lọc danh mục dạng **Pill Filter Chips** thông minh (Công nghệ, Kinh tế, Du lịch, Ngôn ngữ, Xã hội, Nghệ thuật, Y Dược).
   - Tìm kiếm thời gian thực theo tên ngành và mã ngành.
   - Hiển thị song song: Học phí gốc & **Học phí HK1 sau ưu đãi 50%** (nằm gọn trên 1 dòng, số liệu rõ ràng).
   - Modal xem chi tiết tổ hợp môn xét tuyển, số tín chỉ và cơ hội việc làm.
4. **Công Cụ Tính Điểm Xét Tuyển Học Bạ & Dự Toán Học Phí**:
   - Tự động tính điểm tổ hợp 3 môn và đối chiếu ngưỡng sàn 18.0 điểm.
   - Dự toán học phí học kỳ 1 sau giảm 50% ngay lập tức.
5. **5 Phương Thức Tuyển Sinh 2026**:
   - Hướng dẫn điều kiện nộp học bạ, điểm thi tốt nghiệp THPT, kỳ thi ĐGNL ĐHQG TP.HCM, tuyển thẳng và thi năng khiếu.
6. **Hệ Thống Campus Hiện Đại**:
   - Quần thể HungHau Campus 60.000m², Beethoven Grand Auditorium, Smart Classroom.
7. **Form Đăng Ký Xét Tuyển Trực Tuyến**:
   - Tự động sinh mã hồ sơ ưu tiên (`VHU-2026-XXXXXX`) và hiển thị Modal chúc mừng thành công.

---

## 🛠️ Công Nghệ Sử Dụng

- **Frontend**: HTML5 ngữ nghĩa, CSS3 hiện đại (CSS Variables, Flexbox, CSS Grid, Glassmorphism).
- **Typography**: 
  - Tiêu đề: `Playfair Display` (Serif sang trọng, học thuật).
  - Thân bài & Chữ số: `Plus Jakarta Sans` & `Inter` với `font-variant-numeric: tabular-nums lining-nums`.
- **Icons**: Font Awesome 6 Pro / Free CDN.
- **Dữ liệu**: Cơ sở dữ liệu 44 ngành trích xuất trực tiếp từ API Cổng tuyển sinh VHU.

---

## 🚀 Hướng Dẫn Chạy Cục Bộ (Local)

Chỉ cần chạy lệnh sau trên PowerShell hoặc Terminal:

```bash
cd D:\VHU
python -m http.server 8080
```

Mở trình duyệt truy cập: [http://localhost:8080](http://localhost:8080)

---

## 📁 Cấu Trúc Thư Mục

```text
D:\VHU
├── index.html                  # Giao diện chính của Landing Page
├── styles.css                  # Toàn bộ CSS Design Tokens & Animation
├── app.js                      # Logic lọc ngành, tính điểm, form đăng ký, modal
├── majors-data.js              # Database 44 ngành học VHU 2026
├── assets/                     # Hình ảnh logo, campus, phòng học, hội trường
├── BAOCAO_KIEMTRA_GIUAKY_VHU.docx # File Word nộp bài kiểm tra giữa kỳ
├── BAOCAO_KIEMTRA_GIUAKY_VHU.md   # Bản báo cáo Markdown
└── README.md                   # Tài liệu dự án
```

---
© 2026 Trường Đại học Văn Hiến (VHU) • HungHau Holdings.
