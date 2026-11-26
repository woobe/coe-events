#!/usr/bin/env bash
cd /home/joe/repo_dev/coe-events/research/montreal/city/geocode
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
while IFS='|' read -r vid q enc; do
  [ -z "$vid" ] && continue
  code=$(curl -sS -m 30 -A "$UA" -H "Accept: application/json" -H "Referer: https://www.openstreetmap.org/" \
    "https://nominatim.openstreetmap.org/search?q=${enc}&format=jsonv2&limit=3&addressdetails=1&extratags=1" \
    -o "raw3-${vid}.json" -w "%{http_code}")
  echo "$vid $code"
  sleep 1.3
done < /home/joe/repo_dev/coe-events/research/montreal/city/geocode-queries3-enc.txt
