import pandas as pd
import json

# Try to read the CSV with multiple encodings
encodings = ['utf-8', 'latin-1', 'cp1252', 'utf-16']
df = None
enc_used = None
for enc in encodings:
    try:
        df = pd.read_csv('doses.csv', encoding=enc, nrows=20, sep=None, engine='python')
        enc_used = enc
        break
    except Exception as e:
        print(f"  Failed with {enc}: {e}")

if df is None:
    print("Could not read CSV with any encoding!")
else:
    print(f"Encoding used: {enc_used}")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst 20 rows:")
    print(df.to_string())
