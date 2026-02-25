import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Localidad": [
        "Las Joyas", 
        "Victoria de Durango", 
        "La Guajolota", 
        "Colonia Hidalgo", 
        "La Joya", 
        "Gómez Palacio", 
        "Vicente Guerrero", 
        "Cihuacora"
    ],
    "Casos": [20, 18, 8, 3, 2, 1, 1, 1],
    "Lat": [23.3667, 24.0277, 23.3156, 24.1611, 23.3600, 25.5611, 23.7344, 23.4144],
    "Lon": [-104.5500, -104.6532, -104.4925, -104.5714, -104.5450, -103.4981, -103.9850, -104.6461]
}

df = pd.DataFrame(data)

def get_color(casos):
    if casos >= 10: return "red"
    if casos >= 5: return "orange"
    if casos >= 2: return "gold"
    return "green"

colors = [get_color(c) for c in df["Casos"]]
sizes = [c * 50 for c in df["Casos"]]

plt.figure(figsize=(10, 8))
plt.style.use('dark_background')

# Scatter plot representing the map
scatter = plt.scatter(df["Lon"], df["Lat"], s=sizes, c=colors, alpha=0.7, edgecolors='white', linewidth=1)

# Add labels
for i, txt in enumerate(df["Localidad"]):
    plt.annotate(f"{txt} ({df['Casos'][i]})", (df["Lon"][i], df["Lat"][i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='white')

plt.title("Mapa de Priorización de Vacunación - Sarampión 2026", fontsize=14, pad=20)
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.grid(True, linestyle='--', alpha=0.3)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Muy Alta (10+)', markerfacecolor='red', markersize=15),
    Line2D([0], [0], marker='o', color='w', label='Alta (5-9)', markerfacecolor='orange', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Media (2-4)', markerfacecolor='gold', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='Baja (1)', markerfacecolor='green', markersize=5),
]
plt.legend(handles=legend_elements, loc='upper left', title="Niveles de Prioridad")

# Save path
save_path = r"C:\Users\aicil\.gemini\antigravity\brain\338a7255-3ee4-4763-99cd-c0651dfc32bc\mapa_estatico_priorizacion.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Static map saved to {save_path}")
