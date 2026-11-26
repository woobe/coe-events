try:
    import requests; print("requests", requests.__version__)
except Exception as e: print("no requests", e)
try:
    import bs4; print("bs4", bs4.__version__)
except Exception as e: print("no bs4", e)
