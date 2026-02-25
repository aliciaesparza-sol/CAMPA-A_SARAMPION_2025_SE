import pandas as pd
import json

def inspect_and_save():
    encodings = ['latin-1', 'utf-8', 'cp1252']
    seps = [',', ';', '\t', '|']
    
    df = None
    enc_used = 'latin-1'
    sep_used = ','
    
    for enc in encodings:
        for sep in seps:
            try:
                tmp = pd.read_csv('doses.csv', encoding=enc, sep=sep, nrows=5, engine='python')
                if len(tmp.columns) > 3:
                    df = tmp
                    enc_used = enc
                    sep_used = sep
                    break
            except:
                pass
        if df is not None:
            break
    
    # Read full file
    df_full = pd.read_csv('doses.csv', encoding=enc_used, sep=sep_used, engine='python', header=None)
    
    info = {
        'encoding': enc_used,
        'sep': sep_used,
        'total_rows': len(df_full),
        'total_cols': len(df_full.columns),
        'first_5_rows': [],
        'all_cols_unique_values': {}
    }
    
    # First 5 rows as list
    for i in range(min(5, len(df_full))):
        row = [str(v) for v in df_full.iloc[i].tolist()]
        info['first_5_rows'].append(row)
    
    # Unique values in first 10 columns
    for c in range(min(10, len(df_full.columns))):
        vals = df_full.iloc[:, c].dropna().astype(str).unique().tolist()[:30]
        info['all_cols_unique_values'][str(c)] = vals
    
    # Find rows containing 'SRP' or 'SSA' or 'DURANGO'
    def find_rows_by_keyword(keyword, max_results=20):
        mask = df_full.apply(lambda x: x.astype(str).str.contains(keyword, case=False, na=False, regex=False)).any(axis=1)
        rows = df_full[mask].head(max_results)
        result = []
        for _, row in rows.iterrows():
            result.append([str(v) for v in row.tolist()])
        return result
    
    info['rows_with_SRP'] = find_rows_by_keyword('SRP')
    info['rows_with_SSA'] = find_rows_by_keyword('SSA')
    info['rows_with_DURANGO'] = find_rows_by_keyword('DURANGO')
    
    with open('csv_info.json', 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
    
    print(f"Saved. Encoding={enc_used}, Sep='{sep_used}', rows={len(df_full)}, cols={len(df_full.columns)}")

inspect_and_save()
