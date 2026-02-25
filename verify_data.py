import pandas as pd
import sys
import json

def extract_and_verify():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        
        # Exact sheet names from previous run
        # ['PoblaciónTotal 2026', 'Pob META', 'Dosis aplicadas', 'Susceptibles']
        
        results = {}
        # We need specific columns. Let's find Durango row and identify values.
        
        # 1. Poblacion 2026
        df_pop = pd.read_excel(file_path, sheet_name='PoblaciónTotal 2026')
        dur_pop = df_pop[df_pop.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        # Usually total is in a specific column or is the largest number.
        results['Poblacion 2026'] = max([v for v in dur_pop.iloc[0] if isinstance(v, (int, float)) and not pd.isna(v)])

        # 2. Meta
        df_meta = pd.read_excel(file_path, sheet_name='Pob META')
        dur_meta = df_meta[df_meta.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        results['Poblacion Meta'] = max([v for v in dur_meta.iloc[0] if isinstance(v, (int, float)) and not pd.isna(v)])

        # 3. Aplicadas
        df_apl = pd.read_excel(file_path, sheet_name='Dosis aplicadas')
        dur_apl = df_apl[df_apl.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        results['Dosis Aplicadas'] = max([v for v in dur_apl.iloc[0] if isinstance(v, (int, float)) and not pd.isna(v)])

        # 4. Susceptibles
        df_sus = pd.read_excel(file_path, sheet_name='Susceptibles')
        dur_sus = df_sus[df_sus.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        results['Poblacion Susceptible'] = max([v for v in dur_sus.iloc[0] if isinstance(v, (int, float)) and not pd.isna(v)])

        # METHODOLOGY
        # Look for headers or descriptive text in Susceptibles
        df_sus_text = pd.read_excel(file_path, sheet_name='Susceptibles', header=None, nrows=10)
        methodology_lines = []
        for i in range(len(df_sus_text)):
            line = " ".join(df_sus_text.iloc[i].fillna("").astype(str)).strip()
            if line:
                methodology_lines.append(line)
        
        # Manual check for common methodology in these files:
        # Susceptibles = Meta - Aplicadas (often)
        # Let's verify if that holds for Durango
        calc_sus = results['Poblacion Meta'] - results['Dosis Aplicadas']
        is_simple_subtraction = abs(calc_sus - results['Poblacion Susceptible']) < 5 # Allowance for rounding
        
        final_report = {
            "Data": results,
            "Methodology_Found": methodology_lines,
            "Internal_Verification_Met_Minus_Apl": f"{results['Poblacion Meta']} - {results['Dosis Aplicadas']} = {calc_sus} (Actual: {results['Poblacion Susceptible']})",
            "Calculation_Logic": "Población Susceptible = Población Meta - Dosis Aplicadas" if is_simple_subtraction else "Población Susceptible (Calculated value from file)"
        }
        
        print("FINAL_JSON_START")
        print(json.dumps(final_report, indent=2))
        print("FINAL_JSON_END")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    extract_and_verify()
