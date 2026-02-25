import pandas as pd
import unicodedata

def normalize(s):
    if pd.isna(s):
        return ""
    return ''.join(c for c in unicodedata.normalize('NFD', str(s).upper()) if unicodedata.category(c) != 'Mn').strip()

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"
df = pd.read_excel(file_path)

# Population Data (Total Population)
# Factor < 49 years: 0.811
factor = 0.811

# Key: Normalized Name (Colony or Locality) -> Value: Total Population
population_map = {
    'FELIPE ANGELES': 2140,
    'LA GUAJOLOTA': 380,
    'GUAJOLOTA': 380, # Variant
    'COLONIA HIDALGO': 2230,
    'HIDALGO': 2230, # Variant if strictly colony name
    'INDEPENDENCIA': 1350,
    'HECTOR MAYAGOITIA': 1750, # Durango Ampliacion
    'LEGISLADORES': 2040, # Estimated average of Durango colonies
    'VICENTE GUERRERO': 17967,
    'GOMEZ PALACIO': 301742 # Total muncipality/city if used as locality fallback? Or maybe just locality? 
    # Gomez Palacio locality population is ~301k. 
}

# Apply mapping
def get_population(row):
    colony = normalize(row['COLONIA'])
    locality = normalize(row['Localidad de residencia'])
    
    pop_total = 0
    
    if colony in population_map:
        pop_total = population_map[colony]
    elif locality in population_map:
        pop_total = population_map[locality]
    
    if pop_total > 0:
        return int(pop_total * factor)
    return pd.NA

# Find the target column safely
target_col = None
for col in df.columns:
    if "Poblaci" in col and "<49" in col:
        target_col = col
        break

if target_col:
    print(f"Updating column: {target_col}")
    df[target_col] = df.apply(get_population, axis=1)
    
    # Save
    output_path = file_path # Overwrite as requested or save new? User implied "poner" in this file.
    # I will save to a new file first to be safe and verify.
    output_path_verified = file_path.replace(".xlsx", "_updated.xlsx")
    df.to_excel(output_path_verified, index=False)
    print(f"File saved to {output_path_verified}")
    print(df[[target_col, 'COLONIA', 'Localidad de residencia']].head(10))
else:
    print("Target column not found.")
