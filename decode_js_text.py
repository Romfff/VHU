import re
import json

with open('scrape_info.py') as f:
    pass

import urllib.request, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://tuyensinh.vhu.edu.vn/static/js/main.cf3b011f.js", headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    raw_bytes = r.read()

# decode unicode escapes
text = raw_bytes.decode('utf-8', errors='ignore')

# Decode \uXXXX and \xXX escapes
def decode_escapes(s):
    try:
        return s.encode('latin1').decode('unicode-escape')
    except:
        return s

# Let's find patterns like {title: "...", ...} or arrays of commitments, campuses, etc.
matches = re.findall(r'(\{[^\{\}]{20,300}\})', text)
decoded_blocks = []
for m in matches:
    if any(k in m for k in ['Campus', 'HungHau', '1800', 'học bổng', 'Cam k', 'hồ sơ', 'phương thức', 'xét tuyển']):
        try:
            d = json.loads(re.sub(r'([a-zA-Z0-9_]+):', r'"\1":', m.replace("'", '"')))
            decoded_blocks.append(d)
        except:
            # simple regex decode
            unescaped = re.sub(r'\\u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1), 16)), m)
            unescaped = re.sub(r'\\x([0-9a-fA-F]{2})', lambda x: chr(int(x.group(1), 16)), unescaped)
            decoded_blocks.append(unescaped)

with open('decoded_vhu_info.txt', 'w', encoding='utf-8') as f:
    for item in decoded_blocks:
        f.write(str(item) + '\n---\n')

print(f"Decoded {len(decoded_blocks)} blocks.")
