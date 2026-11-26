try:
    from PIL import Image; print("PIL ok", Image.__version__ if hasattr(Image,'__version__') else '')
except Exception as e: print("no PIL", e)
