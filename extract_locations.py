import pandas as pd

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"
df = pd.read_excel(file_path)

print("--- Unique Localities ---")
print(df['Localidad de residencia'].unique())
print("\n--- Unique Colonies ---")
print(df['COLONIA'].unique())
print(f"\nTotal rows: {len(df)}")
