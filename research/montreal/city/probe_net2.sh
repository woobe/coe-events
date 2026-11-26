#!/usr/bin/env bash
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
for u in \
 "https://www.legisquebec.gouv.qc.ca/fr/document/lc/N-1.1" \
 "https://www.legisquebec.gouv.qc.ca/fr/document/lc/F-1.1" \
 "https://laws-lois.justice.gc.ca/eng/acts/L-2/page-14.html" \
 "https://www.canada.ca/en/employment-social-development/services/labour-standards/reports/general-holidays.html" \
 "https://www.cssdm.gouv.qc.ca/calendrier-des-activites-scolaires/" \
 "https://www.emsb.qc.ca/emsb/schools/school-year-calendar" \
 "https://www.cnesst.gouv.qc.ca/fr/conditions-travail/jours-feries" \
 "https://montreal.aitinkerers.org/" \
 "https://canada-holidays.ca/provinces/QC/2027" \
 "https://collectifmtl.com/" \
 "https://sat.qc.ca/en/rent-our-spaces/" \
 "https://crewcollectivecafe.com/en/crew/main-venue" \
 "https://espaceaxc.com/en/" \
 "https://www.district3.co/about" \
 "https://www.lewagon.com/montreal" \
 ; do
  code=$(curl -sS -L --http1.1 -m 30 -A "$UA" -H "Accept-Language: en-CA,en;q=0.9,fr;q=0.8" -o /tmp/pb -w "%{http_code} %{size_download}" "$u" 2>/dev/null)
  echo "$code  $u"
done
