import pandas as pd

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"
try:
    df = pd.read_excel(file_path)
    print("Columns found:")
    for col in df.columns:
        print(f"- {col}")
    print("\nFirst 3 rows:")
    print(df.head(3).to_string())
except Exception as e:
    print(f"Error reading Excel file: {e}")
