import pandas as pd
import os

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\COBERTURA DE VACUNACIÓN\COBERTURAS POR JURISDICCIÓN SARAMPIÓN 13.07.2025.xlsx"

print(f"--- Inspecting {os.path.basename(file_path)} ---")
try:
    xls = pd.ExcelFile(file_path)
    sheet_name = 'LOCALIDADES EN BROTES'
    print(f"  Sheet: {sheet_name}")
    # Read first 20 rows to find headers
    df = pd.read_excel(xls, sheet_name=sheet_name, nrows=20, header=None)
    print(df.to_string())
    
    print("\nAttempting to find meaningful columns...")
    # Look for row with "Colonia" or "Poblacion"
    for idx, row in df.iterrows():
        row_str = " ".join([str(x) for x in row if pd.notnull(x)])
        if "COLONIA" in row_str.upper() or "LOCALIDAD" in row_str.upper():
            print(f"Header candidates at row {idx}: {row.tolist()}")

except Exception as e:
    print(f"  Error reading {file_path}: {e}")
