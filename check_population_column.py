import pandas as pd

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"
df = pd.read_excel(file_path)

# Normalize column names to find the closest match
import unicodedata
def normalize(s):
    return ''.join(c for c in unicodedata.normalize('NFD', str(s)) if unicodedata.category(c) != 'Mn')

found_col = None
for col in df.columns:
    if "Poblaci" in col and "<49" in col:
        found_col = col
        break

if found_col:
    print(f"Column '{found_col}' found.")
    print("Top 10 values:")
    print(df[found_col].head(10))
    print(f"Null count: {df[found_col].isnull().sum()}")
    print(f"Non-null count: {df[found_col].notnull().sum()}")
else:
    print("Column not found.")
