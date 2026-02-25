
import pandas as pd
import sys

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"

try:
    df = pd.read_excel(file_path)
    print("Columns found:")
    for col in df.columns:
        print(f"- {col}")
    print("\nFirst 5 rows:")
    print(df.head().to_string())
except Exception as e:
    print(f"Error reading file {file_path}:\n{e}")
