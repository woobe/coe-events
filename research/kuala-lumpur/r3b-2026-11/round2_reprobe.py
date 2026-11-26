import subprocess, time
URLS = [
 "https://cache.marriott.com/content/dam/marriott-renditions/KULWH/kulwh-greatroom-3044-hor-clsc.jpg",
 "https://cache.marriott.com/content/dam/marriott-renditions/KULWH/kulwh-meeting-facilities-3802-hor-clsc.jpg?output-quality=70&interpolation=progressive-bilinear&downsize=1920px:*",
 "https://cache.marriott.com/content/dam/marriott-renditions/KULWH/kulwh-table-meeting-3801-hor-clsc.jpg",
 "https://cache.marriott.com/content/dam/marriott-renditions/KULXR/kulxr-astor-room-5291-hor-wide.jpg?output-quality=70&interpolation=progressive-bilinear&downsize=2880px:*",
 "https://upload.wikimedia.org/wikipedia/commons/8/85/Kuala_Lumpur_Performing_Arts_Centre_%28230421%29_02.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
 "https://upload.wikimedia.org/wikipedia/commons/8/8f/Kuala_Lumpur_Performing_Arts_Centre_stair_%28230421%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
 "https://upload.wikimedia.org/wikipedia/commons/9/9f/Kuala_Lumpur_Performing_Arts_Centre_%28230421%29_01.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
 "https://upload.wikimedia.org/wikipedia/commons/f/f4/KL_Metropolis_and_MITEC_%28261114%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
 "https://upload.wikimedia.org/wikipedia/commons/f/fe/Kuala_Lumpur_Performing_Arts_Centre_hall_%28230421%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
 "https://worldtradecentrekl.com/wp-content/uploads/2026/02/WTCKL_MERDEKA-HALL_41-scaled.jpg",
 "https://worldtradecentrekl.com/wp-content/uploads/2026/02/WTCKL_MERDEKA-HALL_55-scaled.jpg",
 "https://worldtradecentrekl.com/wp-content/uploads/2026/02/WTCKL_MERDEKA-HALL_71-scaled.jpg",
]
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0 Safari/537.36")
for u in URLS:
    p = subprocess.run(["curl", "-sS", "-L", "-A", UA, "-o", "/dev/null", "--max-time", "60",
                        "-w", "%{http_code} %{size_download}", u],
                       capture_output=True, text=True)
    print(p.returncode, p.stdout.strip(), u.split("/")[-1][:70])
    time.sleep(1.5)
