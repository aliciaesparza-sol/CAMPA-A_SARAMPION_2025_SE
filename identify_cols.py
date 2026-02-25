import pandas as pd
import sys
import os
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_final_report():
    file_path = 'data.xlsx'
    xl = pd.ExcelFile(file_path)

    # ----------------------------------------------------------------
    # Step 1: Read each sheet to find age-group columns for Durango
    # ----------------------------------------------------------------
    # Age groups defined by the user:
    # 6 a 11 meses | 1 año | 18 meses | Rezagados 2 a 12 años | 13 a 19 años | 20 a 39 años | 40 a 49 años
    target_groups_keywords = {
        '6 a 11 meses': ['6', '11', 'mes', '6 a 11', '6-11'],
        '1 año': ['1 año', '1 a?o', '1año', '1 an', '12 mes'],
        '18 meses': ['18 mes', '18m'],
        'Rezagados 2 a 12 años': ['rezag', '2 a 12', '2-12', '2 a?o'],
        '13 a 19 años': ['13 a 19', '13-19', '13 a?o'],
        '20 a 39 años': ['20 a 39', '20-39', '20 a?o'],
        '40 a 49 años': ['40 a 49', '40-49', '40 a?o'],
    }

    sheets_data = {}
    for sn in xl.sheet_names:
        df_raw = pd.read_excel(file_path, sheet_name=sn, header=None, nrows=8)
        
        # Find the header row (row with most text strings)
        best_row = 0
        best_count = 0
        for r in range(min(8, len(df_raw))):
            count = df_raw.iloc[r].apply(lambda x: isinstance(x, str) and len(str(x)) > 0).sum()
            if count > best_count:
                best_count = count
                best_row = r

        df = pd.read_excel(file_path, sheet_name=sn, header=best_row)
        
        # Find Durango row
        mask = df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
        dur_rows = df[mask]
        if dur_rows.empty:
            sheets_data[sn] = {'header_row': best_row, 'columns': list(df.columns), 'durango': None}
        else:
            sheets_data[sn] = {'header_row': best_row, 'columns': list(df.columns), 'durango': dur_rows.iloc[0]}

    # Print column names for each sheet to help identify age groups
    for sn, info in sheets_data.items():
        print(f"\nSheet: {sn}")
        for i, c in enumerate(info['columns']):
            print(f"  Col {i}: '{c}'")
        if info['durango'] is not None:
            print(f"  Durango values: {info['durango'].to_dict()}")

if __name__ == "__main__":
    build_final_report()
