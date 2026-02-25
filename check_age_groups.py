import pandas as pd
import sys

def check_columns():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        
        for sn in xl.sheet_names:
            print(f"\n--- Sheet: {sn} ---")
            # Read top rows to identify headers
            df = pd.read_excel(file_path, sheet_name=sn, header=None, nrows=10)
            print("First 10 rows (header=None):")
            print(df.to_string())
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_columns()
