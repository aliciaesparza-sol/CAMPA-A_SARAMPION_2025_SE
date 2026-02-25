import pypdf
import os

pdf_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\LISTADO CASOS CONFIRMADOS BROTE_SARAMPIÓN 2026 15.02.2026.pdf"

try:
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += f"\n--- PAGE {reader.get_page_number(page)} ---\n"
        full_text += page.extract_text()
    
    with open("extracted_full_text.txt", "w", encoding="utf-8") as f:
        f.write(full_text)
    print("Succesfully extracted text to extracted_full_text.txt")
except Exception as e:
    print(f"Error: {e}")
