import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

endpoints = [
    '/api/slides',
    '/api/tuition',
    '/api/homepage-button-config',
    '/api/form'
]

results = {}
for ep in endpoints:
    url = f"https://tuyensinh.vhu.edu.vn{ep}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            data = r.read().decode('utf-8', errors='ignore')
            try:
                results[ep] = json.loads(data)
            except:
                results[ep] = data[:500]
            print(f"Success fetching {ep}")
    except Exception as e:
        print(f"Error fetching {ep}: {e}")
        results[ep] = str(e)

with open('api_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved api_results.json")
