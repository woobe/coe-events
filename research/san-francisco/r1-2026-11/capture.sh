#!/bin/bash
# capture a URL list into the r1 evidence dir; prints status/size/bytes
cd "$(dirname "$0")" || exit 1
OUT=raw
mkdir -p "$OUT"
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0 Safari/537.36'
while IFS='|' read -r name url; do
  [ -z "$name" ] && continue
  case "$name" in \#*) continue;; esac
  code=$(curl -sL --max-time 45 -A "$UA" -w '%{http_code}' -o "$OUT/$name.raw" "$url")
  size=$(wc -c < "$OUT/$name.raw")
  echo "$name $code $size $url"
done < "$1"
