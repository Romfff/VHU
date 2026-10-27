import re
import json
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://tuyensinh.vhu.edu.vn/static/js/main.cf3b011f.js", headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    js = r.read().decode('utf-8', errors='ignore')

# Extract string literals or objects
# Search for majors (mã ngành, ngành học, etc.)
vietnamese_strings = re.findall(r'["\']([A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝĐa-zàáâãèéêìíòóôõùúýđ0-9\s,\.\-–—\(\)/:]{5,100})["\']', js)
print("Sample vietnamese strings:", len(vietnamese_strings))

# Search for images in JS bundle
img_in_js = re.findall(r'["\'](static/media/[^"\']+\.(?:png|jpg|jpeg|webp|svg))["\']', js)
print("Images in JS bundle:", set(img_in_js))

# Search for external URLs or CDN URLs in JS
cdn_urls = re.findall(r'https?://[^\s"\'`]+\.(?:png|jpg|jpeg|webp|svg)', js)
print("CDN URLs:", set(cdn_urls))

# Search for API endpoints
endpoints = re.findall(r'["\'](/api/[^"\']+)["\']', js)
print("API endpoints:", set(endpoints))

with open('js_strings_sample.txt', 'w', encoding='utf-8') as f:
    for s in vietnamese_strings[:200]:
        f.write(s + '\n')

with open('js_images.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(list(set(img_in_js) | set(cdn_urls)))))
