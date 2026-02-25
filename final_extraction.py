import pandas as pd
import sys
import json

def final_extraction():
    try:
        file_path = 'data.xlsx'
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        print(f"Available sheets: {sheet_names}")
        
        def get_sheet_by_keyword(keyword):
            for sn in sheet_names:
                if keyword.lower() in sn.lower():
                    return sn
            return None

        sheets_to_process = {
            'Poblacion 2026': get_sheet_by_keyword('PoblaciónTotal'),
            'Metas': get_sheet_by_keyword('Metas'),
            'Aplicadas': get_sheet_by_keyword('Aplicadas'),
            'Susceptibles': get_sheet_by_keyword('Susceptibles')
        }
        
        results = {}
        
        for label, sheet_name in sheets_to_process.items():
            if not sheet_name:
                results[label] = "Sheet not found"
                continue
                
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            # Find Durango row
            mask = df.apply(lambda x: x.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
            dur_row = df[mask]
            
            if not dur_row.empty:
                # Find the largest number in the row (likely the total)
                numeric_vals = [val for val in dur_row.iloc[0] if isinstance(val, (int, float)) and not pd.isna(val)]
                if numeric_vals:
                    results[label] = max(numeric_vals)
                else:
                    results[label] = "No numeric data found"
            else:
                results[label] = "Durango not found"

        # Methodology from Susceptibles
        methodology = "Not found"
        sus_sheet = sheets_to_process['Susceptibles']
        if sus_sheet:
            df_sus_raw = pd.read_excel(file_path, sheet_name=sus_sheet, header=None, nrows=20)
            # Flatten the first few rows to look for text
            all_text = []
            for i in range(len(df_sus_raw)):
                row_text = " ".join(df_sus_raw.iloc[i].fillna("").astype(str))
                all_text.append(row_text)
            
            # Look for formula or calculation words
            for line in all_text:
                if any(kw in line.lower() for kw in ['fórmula', 'formula', 'cálculo', 'metodología', '=']):
                    methodology = line
                    # Maybe collect a few lines around it?
                    idx = all_text.index(line)
                    methodology = "\n".join(all_text[max(0, idx-1):min(len(all_text), idx+3)])
                    break
        
        print("--- DATA ---")
        print(json.dumps(results, indent=2))
        print("\n--- METHODOLOGY ---")
        print(methodology)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    final_extraction()
