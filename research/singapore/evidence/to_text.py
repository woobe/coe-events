import sys, re, html as H
p = sys.argv[1]
raw = open(p, encoding='utf-8', errors='replace').read()
raw = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', raw)
raw = re.sub(r'(?is)<!--.*?-->', ' ', raw)
raw = re.sub(r'(?i)<br\s*/?>', '\n', raw)
raw = re.sub(r'(?i)</(p|div|li|tr|h[1-6]|section|article|table|dd|dt|button|a|td|th)>', '\n', raw)
text = re.sub(r'(?s)<[^>]+>', ' ', raw)
text = H.unescape(text)
lines = []
for line in text.splitlines():
    line = re.sub(r'[ \t\r\f\v]+', ' ', line).strip()
    if line:
        lines.append(line)
out = '\n'.join('%4d| %s' % (i+1, l) for i, l in enumerate(lines))
open(sys.argv[2], 'w', encoding='utf-8').write(out)
print(len(lines), 'lines ->', sys.argv[2])
