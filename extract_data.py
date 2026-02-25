import pandas as pd
import sys

def extract_durango_data():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        
        results = {}
        
        for sheet_name in xl.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            
            # Find Durango row
            # Some sheets might have 'DURANGO' in a column named 'Entidad' or 'ESTADO'
            # We search in all columns for the word 'DURANGO'
            mask = df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
            durango_df = df[mask]
            
            if not durango_df.empty:
                results[sheet_name] = durango_df
                print(f"--- Data found for DURANGO in sheet: {sheet_name} ---")
                print(durango_df.to_string())
                print("\n")
            else:
                print(f"--- No DURANGO data found in sheet: {sheet_name} ---")
                # Print first few rows to see structure if Durango not found
                print(df.head(5).to_string())
                print("\n")
                
        # Look for methodology in 'Susceptibles' sheet specifically
        if 'Susceptibles' in xl.sheet_names:
            print("--- Methodology Extraction from 'Susceptibles' ---")
            df_sus = pd.read_excel(file_path, sheet_name='Susceptibles')
            # Look for rows that might be notes (usually at the end or top, or contain "Metodologia", "Calculo", "=", "(", etc.)
            notes_mask = df_sus.apply(lambda x: x.astype(str).str.contains(r'metodología|cálculo|susceptible', case=False, na=False)).any(axis=1)
            notes = df_sus[notes_mask]
            if not notes.empty:
                print("Potential methodology notes found:")
                print(notes.to_string())
            else:
                print("No direct methodology notes found by keyword search.")
            
            # Also just print the first 20 rows of 'Susceptibles' to manually check for a description
            print("\nFirst 20 rows of 'Susceptibles' sheet:")
            print(df_sus.head(20).to_string())

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    extract_durango_data()
