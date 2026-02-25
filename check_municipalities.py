import pandas as pd

file_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"
df = pd.read_excel(file_path)

# Filter for relevant colonies to check their Municipality
interested_colonies = ['HECTOR MAYAGOITIA', 'LEGISLADORES']
subset = df[df['COLONIA'].isin(interested_colonies) | df['Localidad de residencia'].isin(interested_colonies)]

print(subset[['Localidad de residencia', 'Municipio de residencia', 'COLONIA']])
