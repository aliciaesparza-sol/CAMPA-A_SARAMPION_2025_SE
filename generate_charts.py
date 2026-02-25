import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CAMPAÑA SARAMPIÓN 10 SEMANAS\SRP-SR-2025_22-02-2026 06-41-08.csv"
excel_path = r"C:\Users\aicil\.gemini\antigravity\scratch\COBERTURAS_UPDATED_2025.xlsx"
output_dir = r"C:\Users\aicil\.gemini\antigravity\scratch\charts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Loading data...")
df_csv = pd.read_csv(csv_path, encoding='latin1', low_memory=False)

# Categorize age groups
target_groups = {
    '10-12 a': ['10 A 12'],
    '13-19 a': ['13 A 19'],
    '20-39 a': ['20 A 39'],
    '40-49 a': ['40 A 49']
}

# Find all dose columns
all_cols = df_csv.columns.tolist()
group_cols = {}
all_dose_cols = []
for name, keywords in target_groups.items():
    cols = [c for c in all_cols if any(k in c for k in keywords)]
    group_cols[name] = cols
    all_dose_cols.extend(cols)

# Ensure numeric and fill NaNs for the entire DF
df_csv[all_dose_cols] = df_csv[all_dose_cols].apply(pd.to_numeric, errors='coerce').fillna(0)
df_csv['Total_10_49'] = df_csv[all_dose_cols].sum(axis=1)

# Population Targets (Hardcoded from SE20 Sheet if dynamic extraction is risky)
# Basado en la inspección: Durango Total Meta es ~617k para 10-49?
# Vamos a extraer la Meta de la fila 5, columna 1 (B) que suele ser el Total Estatal
xl = pd.ExcelFile(excel_path)
meta_sheet = pd.read_excel(excel_path, sheet_name='SE20', header=None)
# Buscamos la fila de 'TOTAL ESTADO' o la que tenga el gran total. 
# En la inspección previa, el índice 4 tenía 'META', 'DOSIS', etc.
# Suponiendo que la fila 5 tiene el total.
state_meta = meta_sheet.iloc[5, 1] 
print(f"State Meta (Total 10-49): {state_meta}")

# Aggregate doses by Week (Expanding to 53 weeks)
weeks = list(range(1, 54))
coverage_data = []

cumulative_total = 0
for week in weeks:
    week_df = df_csv[df_csv['SEMANA'] == week]
    week_doses = 0
    group_weekly = {}
    
    for name, cols in group_cols.items():
        doses = week_df[cols].apply(pd.to_numeric, errors='coerce').fillna(0).sum().sum()
        group_weekly[name] = doses
        week_doses += doses
        
    cumulative_total += week_doses
    coverage_pct = (cumulative_total / state_meta) * 100 if state_meta > 0 else 0
    coverage_data.append({
        'Week': f"SE{week}",
        'Semana_Num': week,
        'Weekly_Doses': week_doses,
        'Cumulative_Doses': cumulative_total,
        'Coverage': coverage_pct,
        **group_weekly
    })

df_plot = pd.DataFrame(coverage_data)

# Behavior Analysis
peak_week_row = df_plot.loc[df_plot['Weekly_Doses'].idxmax()]
avg_doses = df_plot[df_plot['Weekly_Doses'] > 0]['Weekly_Doses'].mean()
active_weeks = df_plot[df_plot['Weekly_Doses'] > 0]['Week'].tolist()

analysis = {
    "peak_week": peak_week_row['Week'],
    "peak_doses": int(peak_week_row['Weekly_Doses']),
    "avg_weekly_doses": float(avg_doses),
    "total_doses": int(cumulative_total),
    "final_coverage": float(coverage_pct),
    "start_week": active_weeks[0] if active_weeks else "N/A",
    "end_week": active_weeks[-1] if active_weeks else "N/A"
}

import json
with open(os.path.join(output_dir, 'analysis.json'), 'w') as f:
    json.dump(analysis, f, indent=4)

# Chart 1: Cumulative Coverage (%)
plt.figure(figsize=(15, 7))
plt.plot(df_plot['Semana_Num'], df_plot['Coverage'], marker='.', color='#e63946', linewidth=2)
plt.title('Progreso de Cobertura Acumulada 2025 (10-49 Años) - 53 Semanas', fontsize=14)
plt.xlabel('Semana Epidemiológica', fontsize=12)
plt.ylabel('Cobertura (%)', fontsize=12)
plt.xlim(1, 53)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'cobertura_acumulada_53.png'))

# Chart 2: Doses by Age Group
ax = df_plot.plot(x='Semana_Num', y=list(target_groups.keys()), kind='bar', stacked=True, figsize=(15, 7), width=0.8)
plt.title('Distribución de Dosis por Grupo de Edad (SE1 - SE53)', fontsize=14)
plt.xlabel('Semana Epidemiológica', fontsize=12)
plt.ylabel('Dosis', fontsize=12)
plt.legend(title='Grupo de Edad')
plt.xticks(ticks=range(len(df_plot)), labels=df_plot['Semana_Num'], rotation=90, fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'dosis_por_edad_53.png'))

# Chart 3: Doses by Municipality (Top 20)
muni_agg = df_csv.groupby('MUNICIPIO')['Total_10_49'].sum().sort_values(ascending=True).tail(20)
plt.figure(figsize=(10, 8))
muni_agg.plot(kind='barh', color='#457b9d')
plt.title('Top 20 Municipios por Dosis Aplicadas (10-49 Años)', fontsize=14)
plt.xlabel('Total Dosis', fontsize=12)
plt.ylabel('Municipio', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'dosis_por_municipio_53.png'))

print(f"All charts (53 weeks) including municipality data saved in {output_dir}")
df_plot.to_csv(os.path.join(output_dir, 'chart_data_53.csv'), index=False)
