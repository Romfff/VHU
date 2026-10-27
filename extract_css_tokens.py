import re

with open('tng_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find key class definitions
classes_to_check = [
    'hero', 'display', 'eyebrow', 'lede', 'btn', 'band', 'caps', 
    'glow', 'range', 'markets', 'footer', 'media', 'header', 'drawer'
]

results = {}
for c in classes_to_check:
    matches = re.findall(rf'(\.{c}[^{{]*\{{[^}}]+\}})', css)
    results[c] = matches[:4]

with open('tng_key_styles.css', 'w', encoding='utf-8') as f:
    for c, ms in results.items():
        f.write(f"/* === {c} === */\n")
        f.write("\n".join(ms))
        f.write("\n\n")

print("Saved tng_key_styles.css")
