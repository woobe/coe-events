for m in ['pypdf', 'PyPDF2', 'pdfminer', 'fitz', 'pdfplumber']:
    try:
        __import__(m); print(m, 'OK')
    except Exception as e:
        print(m, 'MISSING')
