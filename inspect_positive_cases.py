import pandas as pd
import os

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS POSITIVOS A SARAMPION  DGO 2025.xlsx"

print(f"--- Inspecting {os.path.basename(file_path)} ---")
try:
    xls = pd.ExcelFile(file_path)
    print(f"Sheets: {xls.sheet_names}")
    for sheet_name in xls.sheet_names:
        print(f"  Sheet: {sheet_name}")
        df = pd.read_excel(xls, sheet_name=sheet_name, nrows=20, header=None)
        print(df.to_string())
except Exception as e:
    print(f"  Error reading {file_path}: {e}")
