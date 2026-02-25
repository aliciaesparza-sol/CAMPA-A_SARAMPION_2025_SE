import pypdf
import sys

pdf_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\LISTADO CASOS CONFIRMADOS BROTE_SARAMPIÓN 2026 15.02.2026.pdf"

try:
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    print("--- START OF TEXT ---")
    # Print only first 1000 characters to verify
    print(text[:1000])
    print("--- END OF TEXT ---")
except Exception as e:
    print(f"Error: {e}")
