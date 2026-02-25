import pandas as pd
import json
import sys

def discover_all():
    src = 'data.xlsx'
    SHEETS = {
        'pob':  'PoblaciónTotal 2026',
        'meta': 'Pob META',
        'apl':  'Dosis aplicadas',
        'sus':  'Susceptibles',
    }
    all_info = {}
    for key, sn in SHEETS.items():
        df_raw = pd.read_excel(src, sheet_name=sn, header=None, nrows=10)
        best_row = max(range(min(8, len(df_raw))),
                       key=lambda r: df_raw.iloc[r].apply(
                           lambda x: isinstance(x, str) and len(str(x).strip()) > 1).sum())
        df = pd.read_excel(src, sheet_name=sn, header=best_row)
        df.columns = [str(c).strip() for c in df.columns]
        
        # All column names
        cols = df.columns.tolist()
        
        # Durango row
        mask = df.apply(lambda c: c.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
        dur = df[mask]
        dur_dict = {}
        if not dur.empty:
            row = dur.iloc[0]
            dur_dict = {str(col): (None if pd.isna(val) else val) for col, val in row.items()}
        
        all_info[key] = {
            'sheet': sn,
            'header_row': best_row,
            'columns': cols,
            'durango': dur_dict
        }
    
    with open('all_info.json', 'w', encoding='utf-8') as f:
        json.dump(all_info, f, ensure_ascii=False, indent=2, default=str)
    print("Saved to all_info.json")

discover_all()
