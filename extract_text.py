import re
import json

with open('extract_js_details.py') as f:
    pass

import urllib.request, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://tuyensinh.vhu.edu.vn/static/js/main.cf3b011f.js", headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    js = r.read().decode('utf-8', errors='ignore')

# Search for sections in JS
matches = re.findall(r'phương thức [0-9]+[^"\']+', js, re.IGNORECASE)
print("Phuong thuc matches:", len(matches))

# Find paragraphs or content blocks
blocks = re.findall(r'\{[^{}]*?"title"[^{}]*?\}', js)
print("Blocks with title:", len(blocks))

# Find any text around "Thành nhân" or "học bổng" or "xét học bạ"
snippets = re.findall(r'.{0,100}(?:Thành nhân|học bổng|xét tuyển|học phí|HungHau|Bình Chánh|1800.{0,10}1568).{0,100}', js)
print("Snippets found:", len(snippets))
with open('extracted_snippets.txt', 'w', encoding='utf-8') as f:
    for s in set(snippets[:100]):
        f.write(s.strip() + '\n---\n')

print("Saved extracted_snippets.txt")
