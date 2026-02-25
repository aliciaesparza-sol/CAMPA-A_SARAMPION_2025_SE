import pandas as pd
import os

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\COBERTURA DE VACUNACIÓN\COBERTURAS POR JURISDICCIÓN SARAMPIÓN 13.07.2025.xlsx"

print(f"--- Inspecting {os.path.basename(file_path)} ---")
try:
    xls = pd.ExcelFile(file_path)
    print(f"Sheets: {xls.sheet_names}")
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, nrows=5)
        print(f"  Sheet: {sheet_name}")
        print(f"  Columns: {list(df.columns)}")
        # Check if any column looks like 'Colonia' or 'Population'
        for col in df.columns:
            if "colon" in str(col).lower() or "pob" in str(col).lower():
                print(f"    Potential match: {col}")
                print(df[col].head())
except Exception as e:
    print(f"  Error reading {file_path}: {e}")
