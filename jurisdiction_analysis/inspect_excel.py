import pandas as pd
import os

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\MICROPLANIFICACION\JURISDICCIÓN 1\JURISDICCIÓN SANITARIA NO. 1.xlsx"

try:
    xl = pd.ExcelFile(file_path)
    print(f"File found: {file_path}")
    print(f"Sheet names: {xl.sheet_names}")

    for sheet in xl.sheet_names:
        print(f"\n--- Sheet: {sheet} ---")
        df = xl.parse(sheet, nrows=5)
        print(df.columns.tolist())
        print(df.head())
        print("-" * 30)

except Exception as e:
    print(f"Error reading file: {e}")
