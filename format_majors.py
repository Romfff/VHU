import json

with open('api_results.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

raw_majors = d['/api/tuition']['data']

def safe_int(val, default=0):
    try:
        if isinstance(val, (int, float)):
            return int(val)
        if isinstance(val, str):
            clean = val.replace(',', '').replace('.', '').strip()
            return int(clean) if clean else default
        return default
    except:
        return default

def categorize(name):
    n = name.lower()
    if any(k in n for k in ['tin học', 'công nghệ thông tin', 'mạng máy tính', 'phần mềm', 'dữ liệu', 'trí tuệ nhân tạo', 'khoa học máy tính', 'hệ thống thông tin', 'vi mạch', 'bán dẫn', 'kỹ thuật']):
        if 'môi trường' in n or 'sinh học' in n or 'thực phẩm' in n:
            return 'Công nghệ sinh học & Thực phẩm'
        return 'Công nghệ & Kỹ thuật'
    if any(k in n for k in ['kinh tế', 'quản trị', 'marketing', 'kế toán', 'tài chính', 'thương mại', 'kinh doanh', 'nhân lực', 'bất động sản', 'luật', 'logistics']):
        return 'Kinh tế & Quản trị'
    if any(k in n for k in ['du lịch', 'khách sạn', 'nhà hàng', 'lữ hành', 'dịch vụ']):
        return 'Du lịch & Dịch vụ'
    if any(k in n for k in ['ngôn ngữ', 'việt nam học', 'văn học', 'xã hội', 'tâm lý', 'truyền thông', 'quan hệ công chúng', 'quốc tế', 'đông phương']):
        if 'truyền thông' in n or 'quan hệ công chúng' in n:
            return 'Truyền thông & Xã hội'
        return 'Ngôn ngữ & Khoa học Xã hội'
    if any(k in n for k in ['thanh nhạc', 'piano', 'đạo diễn', 'điện ảnh', 'nghệ thuật', 'âm nhạc', 'hội họa', 'đồ họa']):
        return 'Nghệ thuật & Sáng tạo'
    if any(k in n for k in ['y', 'dược', 'điều dưỡng', 'y tế', 'sức khỏe']):
        return 'Y Dược & Sức khỏe'
    return 'Kinh tế & Quản trị'

def get_combinations(category, name):
    n = name.lower()
    if 'công nghệ' in n or 'máy tính' in n or 'xây dựng' in n or 'kỹ thuật' in n:
        return ['A00 (Toán, Lý, Hóa)', 'A01 (Toán, Lý, Anh)', 'D01 (Toán, Văn, Anh)', 'C01 (Toán, Văn, Lý)']
    if 'ngôn ngữ' in n:
        return ['D01 (Toán, Văn, Anh)', 'D14 (Văn, Sử, Anh)', 'D15 (Văn, Địa, Anh)', 'A01 (Toán, Lý, Anh)']
    if 'thanh nhạc' in n or 'piano' in n or 'đạo diễn' in n:
        return ['N00 (Văn, Năng khiếu 1, Năng khiếu 2)', 'H00 (Văn, Năng khiếu)']
    if 'điều dưỡng' in n or 'dược' in n or 'sinh học' in n or 'thực phẩm' in n:
        return ['B00 (Toán, Hóa, Sinh)', 'A00 (Toán, Lý, Hóa)', 'D07 (Toán, Hóa, Anh)', 'B08 (Toán, Sinh, Anh)']
    return ['A00 (Toán, Lý, Hóa)', 'A01 (Toán, Lý, Anh)', 'D01 (Toán, Văn, Anh)', 'C00 (Văn, Sử, Địa)']

majors_formatted = []
for m in raw_majors:
    name = str(m.get('TÊN NGÀNH HỌC', '')).strip()
    code = str(m.get('MÃ NGÀNH', '')).strip()
    group = str(m.get('Nhóm ngành', 'Nhóm 1')).strip()
    credits = safe_int(m.get('Số tín chỉ'), 136)
    fee_raw = safe_int(m.get(' HỌC PHÍ HỌC KỲ 1 '), 15000000)
    fee_discount = safe_int(m.get(' HỌC PHÍ HK1 SAU HỖ TRỢ 50% '), int(fee_raw / 2))
    cat = categorize(name)
    combos = get_combinations(cat, name)
    
    majors_formatted.append({
        'id': m.get('STT', len(majors_formatted) + 1),
        'name': name,
        'code': code,
        'group': group,
        'category': cat,
        'credits': credits,
        'fee': fee_raw,
        'feeDiscount': fee_discount,
        'combinations': combos,
        'description': f'Chương trình đào tạo cử nhân chất lượng cao ngành {name} tại Đại học Văn Hiến định hướng ứng dụng thực tế, gắn kết trực tiếp với doanh nghiệp ngay từ năm 2.'
    })

with open('majors_clean.json', 'w', encoding='utf-8') as f:
    json.dump(majors_formatted, f, ensure_ascii=False, indent=2)

print(f"Successfully processed and saved {len(majors_formatted)} majors.")
