import pandas as pd
import os

files_to_inspect = [
    r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx",
    r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS POSITIVOS A SARAMPION  DGO 2025.xlsx"
]

for file_path in files_to_inspect:
    print(f"--- Inspecting {os.path.basename(file_path)} ---")
    try:
        xls = pd.ExcelFile(file_path)
        print(f"Sheets: {xls.sheet_names}")
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name, nrows=5)
            print(f"  Sheet: {sheet_name}")
            print(f"  Columns: {list(df.columns)}")
    except Exception as e:
        print(f"  Error reading {file_path}: {e}")
