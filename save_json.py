import pandas as pd
import json

def show_cols():
    src = 'data.xlsx'
    SHEETS = {
        'pob':  'PoblaciónTotal 2026',
        'meta': 'Pob META',
        'apl':  'Dosis aplicadas',
        'sus':  'Susceptibles',
    }
    output = {}
    for key, sn in SHEETS.items():
        df_raw = pd.read_excel(src, sheet_name=sn, header=None, nrows=10)
        best_row = max(range(min(8, len(df_raw))),
                       key=lambda r: df_raw.iloc[r].apply(
                           lambda x: isinstance(x, str) and len(str(x).strip()) > 1).sum())
        df = pd.read_excel(src, sheet_name=sn, header=best_row)
        df.columns = [str(c).strip() for c in df.columns]
        mask = df.apply(lambda c: c.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
        dur = df[mask]
        if not dur.empty:
            row = dur.iloc[0]
            output[sn] = {str(col): str(val) for col, val in row.items()}
    
    with open('durango_detail.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print("Done. Check durango_detail.json")

show_cols()
