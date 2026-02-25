import folium
import pandas as pd
from geopy.geocoders import Nominatim
import time

# Data from previous step
data = {
    "Localidad": [
        "LAS JOYAS, MEZQUITAL, DURANGO", 
        "VICTORIA DE DURANGO, DURANGO", 
        "LA GUAJOLOTA, MEZQUITAL, DURANGO", 
        "COLONIA HIDALGO, DURANGO", 
        "LA JOYA, MEZQUITAL, DURANGO", 
        "GÓMEZ PALACIO, DURANGO", 
        "VICENTE GUERRERO, DURANGO", 
        "CIHUACORA, MEZQUITAL, DURANGO"
    ],
    "Casos": [20, 18, 8, 3, 2, 1, 1, 1]
}

df = pd.DataFrame(data)

def get_color(casos):
    if casos >= 10: return "red"
    if casos >= 5: return "orange"
    if casos >= 2: return "yellow"
    return "green"

geolocator = Nominatim(user_agent="prioritization_map_generator")

# Manual overrides for hard-to-find localities in Durango
coords_cache = {
    "LAS JOYAS, MEZQUITAL, DURANGO": (23.3667, -104.5500), # Approx
    "VICTORIA DE DURANGO, DURANGO": (24.0277, -104.6532),
    "LA GUAJOLOTA, MEZQUITAL, DURANGO": (23.3156, -104.4925),
    "COLONIA HIDALGO, DURANGO": (24.1611, -104.5714),
    "LA JOYA, MEZQUITAL, DURANGO": (23.3667, -104.5500), # Same as Las Joyas for mapping
    "GÓMEZ PALACIO, DURANGO": (25.5611, -103.4981),
    "VICENTE GUERRERO, DURANGO": (23.7344, -103.9850),
    "CIHUACORA, MEZQUITAL, DURANGO": (23.4144, -104.6461)
}

# Create map centered in Durango
m = folium.Map(location=[24.0, -104.5], zoom_start=7, tiles="cartodbpositron")

for _, row in df.iterrows():
    loc = row["Localidad"]
    cases = row["Casos"]
    color = get_color(cases)
    
    # Try cache first
    position = coords_cache.get(loc)
    
    if position:
        folium.CircleMarker(
            location=position,
            radius=5 + (cases * 1.5), # Scale radius by cases
            popup=f"<b>{loc}</b><br>Casos: {cases}<br>Prioridad: {color.capitalize()}",
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6
        ).add_to(m)

# Save map
map_path = r"C:\Users\aicil\.gemini\antigravity\brain\338a7255-3ee4-4763-99cd-c0651dfc32bc\prioritization_map.html"
m.save(map_path)
print(f"Map saved to {map_path}")
