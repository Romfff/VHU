import re
import json

with open('vhu_main.html', 'r', encoding='utf-8') as f:
    vhu_main = f.read()

# Find image URLs in vhu_main
images = re.findall(r'(https?://[^\s"\'<>]+\.(?:png|jpg|jpeg|webp|svg))', vhu_main)
print(f"Images in vhu_main: {len(images)}")
with open('vhu_images.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(list(set(images)))))

# Look inside the JS bundle for admissions majors, tuition, etc.
with open('scrape_info.py', 'r', encoding='utf-8') as f:
    pass

import urllib.request, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# Let's fetch https://tuyensinh.vhu.edu.vn/tuyen-sinh-dai-hoc-chinh-quy-2026 or similar
# Also check routes inside JS bundle
with open('scrape_info.py') as f:
    pass
