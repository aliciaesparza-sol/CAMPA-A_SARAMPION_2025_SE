import pandas as pd
import json

df = pd.read_csv('doses.csv', encoding='latin-1', sep=',', engine='python')
df.columns = [str(c).strip() for c in df.columns]

# Save all column names
info = {'columns': list(df.columns)}

# Also save unique values for ESTADO and INSTITUCION
info['ESTADO_unique'] = df['ESTADO'].dropna().unique().tolist()
info['INSTITUCION_unique'] = df['INSTITUCION'].dropna().unique().tolist() if 'INSTITUCION' in df.columns else []

# Find all SRP columns
srp_cols = [c for c in df.columns if 'SRP' in c.upper() or 'SR' in c.upper()]
info['srp_columns'] = srp_cols

# Filter Durango + SSA
mask = (df['ESTADO'].astype(str).str.contains('DURANGO', case=False, na=False)) & \
       (df['INSTITUCION'].astype(str).str.contains('SSA', case=False, na=False))
dur_ssa = df[mask]
info['durango_ssa_row_count'] = len(dur_ssa)

# Sum of all SRP columns for Durango+SSA
if srp_cols:
    dur_ssa_srp = dur_ssa[srp_cols].apply(pd.to_numeric, errors='coerce').fillna(0).sum()
    info['durango_ssa_srp_sums'] = {col: int(dur_ssa_srp[col]) for col in srp_cols}

with open('csv_structure.json', 'w', encoding='utf-8') as f:
    json.dump(info, f, ensure_ascii=False, indent=2)
print("Saved to csv_structure.json")
print(f"ESTADO unique: {info['ESTADO_unique'][:10]}")
print(f"SRP cols found: {srp_cols}")
print(f"Durango+SSA rows: {info['durango_ssa_row_count']}")
