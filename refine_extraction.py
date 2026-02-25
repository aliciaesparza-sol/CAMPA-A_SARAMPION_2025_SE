import pandas as pd
import sys

def refine_extraction():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        
        results = {}
        
        # Helper to find column index by keyword
        def find_col(df, keywords):
            for i, col in enumerate(df.columns):
                if any(kw in str(col).lower() for kw in keywords):
                    return i
            # If not in columns, check first 5 rows
            for r in range(min(5, len(df))):
                for c in range(len(df.columns)):
                    if any(kw in str(df.iloc[r, c]).lower() for kw in keywords):
                        return c
            return None

        # 1. Population 2026
        df_pop = pd.read_excel(file_path, sheet_name='PoblaciónTotal 2026')
        durango_pop_row = df_pop[df_pop.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        # Look for a number that looks like population (usually large)
        pop_val = None
        if not durango_pop_row.empty:
            for val in durango_pop_row.iloc[0]:
                if isinstance(val, (int, float)) and val > 1000: # Assuming Durango population is > 1000
                    pop_val = val
                    break
        results['Poblacion 2026'] = pop_val

        # 2. Metas
        df_metas = pd.read_excel(file_path, sheet_name='Metas')
        dur_meta_row = df_metas[df_metas.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        meta_val = None
        if not dur_meta_row.empty:
            # Look for large number
            for val in dur_meta_row.iloc[0]:
                if isinstance(val, (int, float)) and val > 1000:
                    meta_val = val
                    break
        results['Poblacion Meta'] = meta_val

        # 3. Aplicadas
        df_apl = pd.read_excel(file_path, sheet_name='Aplicadas')
        dur_apl_row = df_apl[df_apl.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        apl_val = None
        if not dur_apl_row.empty:
            for val in dur_apl_row.iloc[0]:
                if isinstance(val, (int, float)) and val > 100:
                    apl_val = val
                    break
        results['Dosis Aplicadas'] = apl_val

        # 4. Susceptibles
        df_sus = pd.read_excel(file_path, sheet_name='Susceptibles')
        dur_sus_row = df_sus[df_sus.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)]
        sus_val = None
        if not dur_sus_row.empty:
            for val in dur_sus_row.iloc[0]:
                if isinstance(val, (int, float)) and val > 100:
                    sus_val = val
                    break
        results['Poblacion Susceptible'] = sus_val

        print("--- SUMMARY ---")
        for k, v in results.items():
            print(f"{k}: {v}")

        # METHODOLOGY
        print("\n--- DETAILED SUSCEPTIBLES TOP ROWS ---")
        df_sus_raw = pd.read_excel(file_path, sheet_name='Susceptibles', header=None, nrows=20)
        print(df_sus_raw.to_string())

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    refine_extraction()
