import pandas as pd
import sys

def analyze_susceptibles():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        
        print("--- Analyzing 'Susceptibles' Sheet ---")
        df = pd.read_excel(file_path, sheet_name='Susceptibles')
        
        # Print all columns to understand the name
        print(f"Columns: {df.columns.tolist()}")
        
        # Look for Durango row
        durango_row = df[df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        print("\nDurango Row(s):")
        print(durango_row.to_string())
        
        # Look for methodology text (usually in the first few rows or columns)
        print("\nSearching for methodology description in the entire sheet...")
        top_rows = pd.read_excel(file_path, sheet_name='Susceptibles', header=None, nrows=10)
        print("Top 10 rows (header=None):")
        print(top_rows.to_string())
        
        # Read the file again but look for cell formulas if possible? 
        # (Standard pandas won't show formulas, but we can infer them from column headers)
        
        print("\n--- Analyzing 'Metas' Sheet ---")
        df_metas = pd.read_excel(file_path, sheet_name='Metas')
        durango_metas = df_metas[df_metas.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        print("Durango Metas:")
        print(durango_metas.to_string())
        
        print("\n--- Analyzing 'Aplicadas' Sheet ---")
        df_aplicadas = pd.read_excel(file_path, sheet_name='Aplicadas')
        durango_aplicadas = df_aplicadas[df_aplicadas.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        print("Durango Aplicadas:")
        print(durango_aplicadas.to_string())
        
        print("\n--- Analyzing 'PoblaciónTotal 2026' Sheet ---")
        df_pop = pd.read_excel(file_path, sheet_name='PoblaciónTotal 2026')
        durango_pop = df_pop[df_pop.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        print("Durango Population 2026:")
        print(durango_pop.to_string())

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    analyze_susceptibles()
