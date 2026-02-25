import pandas as pd
import json

# Read CSV
df = pd.read_csv('doses.csv', encoding='latin-1', sep=',', engine='python')
df.columns = [str(c).strip() for c in df.columns]

print(f"Shape: {df.shape}")
print("\nAll column names:")
for i, c in enumerate(df.columns):
    print(f"  [{i}] '{c}'")

# Show unique values of key identifying columns
for col in df.columns[:6]:
    print(f"\nColumn '{col}' unique values:")
    print(df[col].dropna().unique()[:20])

# Find Durango + SSA rows
print("\n\nFiltering Durango + SSA rows...")
for col in df.columns:
    col_lower = col.lower()
    if 'estado' in col_lower or 'entidad' in col_lower or 'institucion' in col_lower or 'inst' in col_lower:
        print(f"\nCandidate identifying column: '{col}'")
        print(df[col].dropna().unique()[:10])

# Try all columns for DURANGO
mask_dur = df.apply(lambda c: c.astype(str).str.contains('DURANGO', case=False, na=False)).any(axis=1)
mask_ssa = df.apply(lambda c: c.astype(str).str.contains('SSA', case=False, na=False)).any(axis=1)

dur_rows = df[mask_dur & mask_ssa]
print(f"\nDurango+SSA rows count: {len(dur_rows)}")
if not dur_rows.empty:
    print("\nFirst 3 Durango+SSA rows:")
    print(dur_rows.head(3).to_string())
