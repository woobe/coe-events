mods = ['bs4', 'lxml', 'requests', 'playwright', 'html5lib']
for m in mods:
    try:
        __import__(m)
        print(m, 'OK')
    except Exception as e:
        print(m, 'MISSING', e)
