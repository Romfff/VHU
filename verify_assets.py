import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

imgs_html = re.findall(r'assets/images/[a-zA-Z0-9_\.\-]+', html)
imgs_js = re.findall(r'assets/images/[a-zA-Z0-9_\.\-]+', js)

all_imgs = set(imgs_html + imgs_js)
print(f"Total unique referenced images: {len(all_imgs)}")
all_ok = True
for img in sorted(all_imgs):
    exists = os.path.exists(img)
    print(f"[{'PASS' if exists else 'FAIL'}] {img}")
    if not exists:
        all_ok = False

if all_ok:
    print("\nALL REFERENCED IMAGES EXIST AND VERIFIED!")
else:
    print("\nSOME IMAGES ARE MISSING!")
