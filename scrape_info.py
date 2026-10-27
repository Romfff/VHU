import urllib.request
import ssl
import re
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Check JS bundle
js_url = "https://tuyensinh.vhu.edu.vn/static/js/main.cf3b011f.js"
print("Fetching JS bundle...")
js = fetch(js_url)
if js:
    print(f"JS bundle length: {len(js)}")
    # Find endpoints
    urls = re.findall(r'https?://[a-zA-Z0-9\.\-_/]+', js)
    vhu_urls = set(u for u in urls if 'vhu' in u or 'api' in u)
    with open('js_endpoints.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(list(vhu_urls))))
    print("Saved js_endpoints.txt, count:", len(vhu_urls))

# Also fetch main VHU site
main_vhu = fetch("https://vhu.edu.vn/")
if main_vhu:
    with open('vhu_main.html', 'w', encoding='utf-8') as f:
        f.write(main_vhu)
    print("Saved vhu_main.html, length:", len(main_vhu))
