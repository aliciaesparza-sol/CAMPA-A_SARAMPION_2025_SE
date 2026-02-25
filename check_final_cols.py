import pandas as pd
import json
import os
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

# ─── Read CSV ────────────────────────────────────────────────────────────────
df_csv = pd.read_csv('doses.csv', encoding='latin-1', sep=',', engine='python')
df_csv.columns = [str(c).strip() for c in df_csv.columns]
csv_cols = list(df_csv.columns)

print("CSV COLUMNS:")
for i, c in enumerate(csv_cols):
    print(f"  [{i}] '{c}'")

# ─── Read Coverage Excel ──────────────────────────────────────────────────────
xl = pd.ExcelFile('cobertura.xlsx')
print(f"\nCobertura sheet names: {xl.sheet_names}")
df_cob = pd.read_excel('cobertura.xlsx', sheet_name=xl.sheet_names[0])
df_cob.columns = [str(c).strip() for c in df_cob.columns]
print(f"\nCobertura columns: {list(df_cob.columns)}")
print(f"\nCobertura data:")
print(df_cob.to_string())
