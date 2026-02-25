import pandas as pd
import json
import os
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ─── Load data ────────────────────────────────────────────────────────────────
df = pd.read_csv('doses.csv', encoding='latin-1', sep=',', engine='python')
df.columns = [str(c).strip() for c in df.columns]

# Load existing coverage file for Population 2026 and Meta
df_cob = pd.read_excel('cobertura.xlsx', sheet_name='Cobertura Durango 2026')
df_cob.columns = [str(c).strip() for c in df_cob.columns]
# Drop last rows if TOTAL or legend
df_cob = df_cob[df_cob['Grupo de Edad'].notna()].copy()
df_cob = df_cob[~df_cob['Grupo de Edad'].astype(str).str.contains('leyenda|TOTAL|Leyenda', case=False, na=False)]

print("Coverage file columns:", df_cob.columns.tolist())
print("Coverage file rows:")
print(df_cob[['Grupo de Edad','Población 2026','Población Meta']].to_string(index=False))

# ─── Identify SRP-SR columns for each age group ───────────────────────────────
# Print all columns with SRP or SR
all_cols = list(df.columns)
print("\nAll CSV columns:")
for i, c in enumerate(all_cols):
    print(f"  [{i}] '{c}'")
