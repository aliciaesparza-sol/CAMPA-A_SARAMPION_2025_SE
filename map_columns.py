import pandas as pd
import sys

def map_columns():
    """
    For each sheet, read with header=None at multiple rows and 
    find which column index corresponds to each age group.
    Print all column headers with their indices.
    """
    file_path = 'data.xlsx'
    xl = pd.ExcelFile(file_path)
    
    for sn in xl.sheet_names:
        print(f"\n{'='*60}\nSHEET: {sn}\n{'='*60}")
        
        # Try to automatically detect where the real header is
        # by reading multiple rows and finding the one with most text
        df_raw = pd.read_excel(file_path, sheet_name=sn, header=None, nrows=8)
        
        # Find the row with the most non-null text values (likely column headers)
        best_row = 0
        best_count = 0
        for r in range(min(8, len(df_raw))):
            count = df_raw.iloc[r].apply(lambda x: isinstance(x, str) and len(str(x)) > 1).sum()
            if count > best_count:
                best_count = count
                best_row = r
        
        # Use that row as header
        df = pd.read_excel(file_path, sheet_name=sn, header=best_row)
        print(f"  Detected header at row: {best_row}")
        print(f"  Columns: {[str(c) for c in df.columns.tolist()]}")
        
        # Find Durango
        mask = df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
        dur = df[mask]
        if not dur.empty:
            print("  --- Durango Values ---")
            print(dur.to_string())

if __name__ == "__main__":
    map_columns()
