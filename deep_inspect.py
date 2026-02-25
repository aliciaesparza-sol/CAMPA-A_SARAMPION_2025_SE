import pandas as pd
import sys

def deep_inspect():
    file_path = 'data.xlsx'
    xl = pd.ExcelFile(file_path)
    
    for sn in xl.sheet_names:
        print(f"\n{'='*60}\nSHEET: {sn}\n{'='*60}")
        
        # Read with no header to show raw content
        df_raw = pd.read_excel(file_path, sheet_name=sn, header=None, nrows=6)
        
        # Show each column index and its values across first rows
        n_cols = len(df_raw.columns)
        print(f"Number of columns: {n_cols}")
        for c in range(n_cols):
            col_vals = [str(v) for v in df_raw.iloc[:, c].tolist() if str(v).strip() not in ('nan', '')]
            if col_vals:
                print(f"  Col {c}: {col_vals}")

if __name__ == "__main__":
    deep_inspect()
