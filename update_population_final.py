import pandas as pd
import unicodedata

def normalize(s):
    if pd.isna(s):
        return ""
    # Normalize to NFD form, strip accents, convert to upper case
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
    'GUAJOLOTA': 380,
    'COLONIA HIDALGO': 2230,
    'HIDALGO': 2230,
    'INDEPENDENCIA': 1350,
    'HECTOR MAYAGOITIA': 1750, 
    'LEGISLADORES': 2040, 
    'VICENTE GUERRERO': 17967,
    'VICTORIA DE DURANGO': 688697, # Fallback for city
    'GOMEZ PALACIO': 301742
}

def get_population(row):
    colony = normalize(row['COLONIA'])
    locality = normalize(row['Localidad de residencia'])
    
    pop_total = 0
    
    # Priority: Colony -> Locality
    if colony in population_map:
        pop_total = population_map[colony]
    elif locality in population_map:
        pop_total = population_map[locality]
    
    if pop_total > 0:
        return int(pop_total * factor)
    return pd.NA

# Find target column
target_col = None
for col in df.columns:
    if "Poblaci" in col and "<49" in col:
        target_col = col
        break

if target_col:
    print(f"Updating column: {target_col}")
    df[target_col] = df.apply(get_population, axis=1)
    
    # Check for remaining NaNs
    nans = df[df[target_col].isna()]
    if not nans.empty:
        print("Rows with missing population data:")
        print(nans[['Localidad de residencia', 'COLONIA']])
    
    # Save to original file
    try:
        df.to_excel(file_path, index=False)
        print(f"Successfully updated and saved to {file_path}")
    except PermissionError:
        print("Error: Permission denied. Close the file if it is open.")
else:
    print("Target column not found.")
