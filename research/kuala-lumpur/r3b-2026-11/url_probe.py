import subprocess, re, sys
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/158.0.0.0 Safari/537.36")
urls = sys.argv[1:]
for u in urls:
    p = subprocess.run(["curl", "-sS", "-k", "-L", "--compressed", "-m", "40", "-A", UA,
                        "-w", "\n%{http_code} %{url_effective}", u],
                       capture_output=True, text=True, timeout=60)
    body, _, meta = p.stdout.rpartition("\n")
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
    title = re.sub(r"\s+", " ", m.group(1)).strip()[:80] if m else ""
    print(f"{meta} | {title!r} | {len(body)}b | {u}")
