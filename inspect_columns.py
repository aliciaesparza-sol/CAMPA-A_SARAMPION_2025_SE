import pandas as pd
import sys

def check_all_sheets():
    file_path = 'data.xlsx'
    xl = pd.ExcelFile(file_path)
    
    for sn in xl.sheet_names:
        print(f"\n{'='*80}")
        print(f"SHEET: {sn}")
        print('='*80)
        # Read without a header first to see raw structure
        df_raw = pd.read_excel(file_path, sheet_name=sn, header=None, nrows=8)
        for r in range(len(df_raw)):
            row_vals = [str(v) for v in df_raw.iloc[r].tolist() if str(v) != 'nan']
            if row_vals:
                print(f"  Row {r}: {row_vals}")
        
        # Also print full Durango row
        df = pd.read_excel(file_path, sheet_name=sn)
        mask = df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
        durango_rows = df[mask]
        if not durango_rows.empty:
            print(f"\n  DURANGO ROW(S):")
            print("  Columns:", df.columns.tolist())
            print(durango_rows.to_string())

if __name__ == "__main__":
    check_all_sheets()
