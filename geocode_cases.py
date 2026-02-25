import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

# Data from User's Table 6: Priorización de zonas por concentración de domicilios registrados
cases_data = [
    {"colonia": "Héctor Mayagoitia", "municipio": "Durango", "cp": "34010", "casos": 3},
    {"colonia": "La Guajolota", "municipio": "Mezquital", "cp": "34985", "casos": 3},
    {"colonia": "Legisladores", "municipio": "Durango", "cp": "34046", "casos": 2},
    {"colonia": "Cielo Vista", "municipio": "Durango", "cp": "34038", "casos": 1},
    {"colonia": "Francisco Javier Mina", "municipio": "Durango", "cp": "34310", "casos": 1},
    {"colonia": "Gobernadores", "municipio": "Durango", "cp": "34045", "casos": 1},
    {"colonia": "Haciendas del Saltito", "municipio": "Durango", "cp": "34105", "casos": 1},
    {"colonia": "Hidalgo", "municipio": "Durango", "cp": "34310", "casos": 1},
    {"colonia": "Laderas del Pedregal", "municipio": "Durango", "cp": "34015", "casos": 1},
    {"colonia": "Loma Dorada Diamante", "municipio": "Durango", "cp": "34105", "casos": 1},
    {"colonia": "Valentín Gómez Farías", "municipio": "Durango", "cp": "34010", "casos": 1},
    {"colonia": "Valentín Gómez Farías", "municipio": "Durango", "cp": "34310", "casos": 1},
    {"colonia": "Independencia (Mártires)", "municipio": "Gómez Palacio", "cp": "35045", "casos": 1},
    {"colonia": "La Guajolota", "municipio": "Mezquital", "cp": "24980", "casos": 1},
    {"colonia": "Santa María de Ocotán", "municipio": "Mezquital", "cp": "34983", "casos": 1},
    {"colonia": "Zona Centro", "municipio": "Vicente Guerrero", "cp": "34890", "casos": 1}
]

geolocator = Nominatim(user_agent="measles_map_v1")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.5)

results = []

for item in cases_data:
    query = f"{item['colonia']}, {item['municipio']}, Durango, Mexico"
    print(f"Geocoding: {query}")
    location = geocode(query)
    
    if location:
        print(f"  Found: {location.latitude}, {location.longitude}")
        item['lat'] = location.latitude
        item['lng'] = location.longitude
    else:
        # Fallback to Municipio, Durango
        print(f"  Not found. Falling back to {item['municipio']}, Durango")
        fallback_query = f"{item['municipio']}, Durango, Mexico"
        fallback_loc = geocode(fallback_query)
        if fallback_loc:
            item['lat'] = fallback_loc.latitude
            item['lng'] = fallback_loc.longitude
        else:
            item['lat'] = 24.0277 # Durango default
            item['lng'] = -104.6532
            
    results.append(item)

df = pd.DataFrame(results)
df.to_csv("case_coordinates.csv", index=False)
print("Geocoding complete. Saved to case_coordinates.csv")
