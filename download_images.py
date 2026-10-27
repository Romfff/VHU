import urllib.request
import ssl
import os
import re

os.makedirs('assets/images', exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# 1. Download images from tuyensinh.vhu.edu.vn
images_ts = [
    'static/media/i33.aabb08b87f24680955f3.webp',
    'static/media/sv_phuongthuc.977f5b582fc255da6b3b.webp',
    'static/media/i11.a96f8697f7e3051d9ab5.webp',
    'static/media/i1.380881c84974e0cb603b.webp',
    'static/media/bg_phuongthuc.f8389b6b6d195276926f.webp',
    'static/media/i3.f3051b04b86006e15f06.webp',
    'static/media/i32.203fa80e171eef70b43f.webp',
    'static/media/i31.b38a4b0e73e2fe5861db.webp',
    'static/media/logovhu.e13815839ed90114f0f9.webp',
    'static/media/i5.9bcb64c7cdb16a84e174.webp',
    'static/media/i43.865bbbe83a3ed794751c.webp',
    'static/media/i12.0a48ef01a69af007905f.webp',
    'static/media/bg_chinh_sach.dba580446f510e79c965.webp',
    'static/media/i44.9959dbd22749a07b452a.webp',
    'static/media/i8.411a68782c270ab991ca.webp',
    'static/media/i30.8bca964dee284d3af44d.webp',
    'static/media/i41.99b78c9c6cf4899ff0b6.webp',
    'static/media/i40.8835ce749c623e075559.webp',
    'static/media/i2.89ee825551a01d8e5ce6.webp',
    'static/media/mess.137b491fcb9dae3b8569.webp',
    'static/media/i22.97217830db9be519d2d8.webp',
    'static/media/khampha3.07727fa505f14f97d2d5.webp',
    'static/media/i4.aa7da4922ed28ffbd26c.webp',
    'static/media/i39.c705863f77fa9754a480.webp',
    'static/media/chinh_sach.96ebf88c56282205ade4.webp',
    'static/media/zalo-icon.42a2f995d8823b9d6865.webp',
    'static/media/logovhu2.71fc35b386816e8e07d5.webp',
    'static/media/i10.5526bc583cee101480e7.webp',
    'static/media/i42.63dcc9b027071ac8ec54.webp',
    'static/media/i9.3198a17071ed48bd86fd.webp',
    'static/media/i45.6304a66b294f2ef5ee08.webp',
    'static/media/i6.a5db9a959279ac7a20da.webp',
    'logo_vhu.png'
]

downloaded = {}
for rel in images_ts:
    url = f"https://tuyensinh.vhu.edu.vn/{rel}"
    fname = os.path.basename(rel)
    local_path = os.path.join('assets/images', fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            with open(local_path, 'wb') as f:
                f.write(r.read())
        downloaded[rel] = local_path
        print(f"Downloaded: {fname}")
    except Exception as e:
        print(f"Failed {rel}: {e}")

# 2. Also download key images from VHU main site
with open('vhu_images.txt', 'r', encoding='utf-8') as f:
    vhu_imgs = [line.strip() for line in f if line.strip()]

count = 0
for u in vhu_imgs:
    if count >= 15:
        break
    if any(k in u.lower() for k in ['banner', 'campus', 'csvc', 'logo', 'sv', 'tuyensinh', 'sinhvien', 'gioithieu']):
        fname = os.path.basename(u.split('?')[0])
        if not fname.endswith(('.png', '.jpg', '.jpeg', '.webp')):
            fname += '.jpg'
        local_path = os.path.join('assets/images', f"main_{fname}")
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
                with open(local_path, 'wb') as f:
                    f.write(r.read())
            count += 1
            print(f"Downloaded main site img: {fname}")
        except Exception as e:
            pass

print(f"Downloaded {len(downloaded)} tuyensinh images and {count} main site images.")
