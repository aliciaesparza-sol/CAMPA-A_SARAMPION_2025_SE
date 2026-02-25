import pandas as pd

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"

try:
    df = pd.read_excel(file_path)
    print("Columns:", df.columns.tolist())
    print("Number of rows:", len(df))
    print("First 3 rows:\n", df.head(3))
except Exception as e:
    print(f"Error reading file: {e}")
