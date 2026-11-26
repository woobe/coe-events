#!/usr/bin/env bash
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
for u in \
 "https://nominatim.openstreetmap.org/search?q=80+Turk+Street%2C+San+Francisco&format=jsonv2&limit=1" \
 "https://lu.ma/montreal" \
 "https://www.eventbrite.ca/d/canada--montreal/tech/" \
 "https://www.meetup.com/find/?keywords=ai&location=ca--montreal" \
 "https://miragather.com/" \
 "https://aitinkerers.org/all_cities" \
 "https://www.canada.ca/en/employment-social-development/services/labour-standards/reports/general-holidays.html" \
 "https://www.cssdm.gouv.qc.ca/" \
 "https://www.emsb.qc.ca/" \
 "https://versaloft.ca/en/evenements-salle-anaia-en/" \
 ; do
  code=$(curl -sS -L -m 25 -A "$UA" -o /tmp/probe_body -w "%{http_code} %{size_download}" "$u" 2>/dev/null)
  echo "$code  $u"
done
