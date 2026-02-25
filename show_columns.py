import openpyxl
import pandas as pd
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter
import sys
import os

def main():
    src  = 'data.xlsx'
    out  = r'C:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CAMPAÑA SARAMPIÓN 10 SEMANAS\Cobertura_Vacunacion_Durango_2026.xlsx'

    # ── 1. Read every sheet using pandas, auto-detecting header ──────────────
    SHEETS = {
        'pob':  'PoblaciónTotal 2026',
        'meta': 'Pob META',
        'apl':  'Dosis aplicadas',
        'sus':  'Susceptibles',
    }

    loaded = {}
    for key, sn in SHEETS.items():
        df_raw = pd.read_excel(src, sheet_name=sn, header=None, nrows=10)
        # Find the row that has the most text strings (column headers)
        best_row = max(range(min(8, len(df_raw))),
                       key=lambda r: df_raw.iloc[r].apply(
                           lambda x: isinstance(x, str) and len(str(x).strip()) > 1).sum())
        df = pd.read_excel(src, sheet_name=sn, header=best_row)
        # Strip column names
        df.columns = [str(c).strip() for c in df.columns]
        loaded[key] = df

    # ── 2. Show all columns so we can identify age-group column names ─────────
    print("Columns per sheet:")
    for k, df in loaded.items():
        print(f"\n  {k}: {df.columns.tolist()}")

    # ── 3. Build a helper to get Durango row ──────────────────────────────────
    def get_dur(df):
        mask = df.apply(
            lambda col: col.astype(str).str.contains('DURANGO', case=False, na=False)
        ).any(axis=1)
        rows = df[mask]
        return rows.iloc[0] if not rows.empty else None

    for k, df in loaded.items():
        dur = get_dur(df)
        if dur is not None:
            print(f"\nDurango row in '{k}':")
            print(dur.to_dict())

if __name__ == "__main__":
    main()
