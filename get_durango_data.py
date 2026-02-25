import pandas as pd
import sys

def get_durango_summary():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        
        sheet_mapping = {
            'PoblaciónTotal 2026': 'Poblacion 2026',
            'Metas': 'Poblacion Meta',
            'Aplicadas': 'Dosis Aplicadas',
            'Susceptibles': 'Poblacion Susceptible'
        }
        
        durango_data = {}
        
        for sheet_name, label in sheet_mapping.items():
            if sheet_name in xl.sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                # Find row with DURANGO
                mask = df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
                durango_row = df[mask]
                if not durango_row.empty:
                    # Capture the whole row for now to see which column is which
                    durango_data[label] = durango_row.iloc[0].to_dict()
                else:
                    durango_data[label] = "NOT FOUND"
            else:
                durango_data[label] = f"Sheet '{sheet_name}' NOT FOUND"
        
        # Methodology check in Susceptibles
        methodology = "Not found in text"
        if 'Susceptibles' in xl.sheet_names:
            df_sus = pd.read_excel(file_path, sheet_name='Susceptibles', header=None)
            # Search for methodology indicators in first 50 rows, all columns
            for i in range(min(50, len(df_sus))):
                row_str = " ".join(df_sus.iloc[i].fillna("").astype(str))
                if any(kw in row_str.lower() for kw in ['metodología', 'cálculo', 'fórmula', 'formula']):
                    methodology = row_str
                    break
        
        print("RESULT_START")
        import json
        print(json.dumps({'data': durango_data, 'methodology': methodology}, indent=2, default=str))
        print("RESULT_END")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_durango_summary()
