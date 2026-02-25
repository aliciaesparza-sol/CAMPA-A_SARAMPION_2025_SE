import pandas as pd
import sys

try:
    xl = pd.ExcelFile('data.xlsx')
    for sn in xl.sheet_names:
        print(f'--- Sheet: {sn} ---')
        df = pd.read_excel('data.xlsx', sheet_name=sn, nrows=20)
        print(df.to_string())
        print('\n')
        
    # Also print any notes or formulas that might be in the 'Susceptibles' sheet
    # or look for a specific 'Durango' row
    for sn in xl.sheet_names:
        df_full = pd.read_excel('data.xlsx', sheet_name=sn)
        # Search for 'DURANGO' in all columns
        mask = df_full.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False)).any(axis=1)
        durango_rows = df_full[mask]
        if not durango_rows.empty:
            print(f'--- Durango Data in {sn} ---')
            print(durango_rows.to_string())
            print('\n')

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
