import pandas as pd
import json

# Deep inspection: try different separators and find the SRP-SR SSA section
encodings = ['latin-1', 'utf-8', 'cp1252']
seps = [',', ';', '\t', '|']

df = None
enc_used = None
sep_used = None

for enc in encodings:
    for sep in seps:
        try:
            tmp = pd.read_csv('doses.csv', encoding=enc, sep=sep, nrows=5, engine='python')
            if len(tmp.columns) > 3:  # More than 3 cols = likely a valid parse
                df = tmp
                enc_used = enc
                sep_used = sep
                break
        except:
            pass
    if df is not None:
        break

print(f"Best parse: encoding={enc_used}, sep='{sep_used}'")
if df is not None:
    print(f"Columns: {list(df.columns)}")
    
    # Now read a larger portion to find 'SRP' or 'SSA' rows
    df_full = pd.read_csv('doses.csv', encoding=enc_used, sep=sep_used, engine='python', header=None, nrows=200)
    print(f"\nTotal columns detected: {len(df_full.columns)}")
    
    # Find rows that contain 'SRP' or 'SSA'
    mask = df_full.apply(lambda x: x.astype(str).str.contains('SRP|SSA|srp|ssa', case=False, regex=True, na=False)).any(axis=1)
    srp_rows = df_full[mask]
    print(f"\nRows containing 'SRP' or 'SSA' (first 30 rows shown):")
    print(srp_rows.head(30).to_string())
    
    # Also save all unique values in the first few columns to understand structure
    for c in range(min(5, len(df_full.columns))):
        unique_vals = df_full.iloc[:, c].dropna().unique()[:20]
        print(f"\nColumn {c} unique values: {unique_vals}")
else:
    print("Could not parse CSV!")
