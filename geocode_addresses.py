import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# File paths
input_file = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026.xlsx"
output_file = r"c:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CASOS NOTIFICADOS\CASOS CONFIRMADOS 2026\Tabla_Casos_Confirmados_Sarampion_2026_with_Coords.xlsx"

def get_coordinates():
    try:
        print("Loading Excel file...")
        df = pd.read_excel(input_file)
        
        # Initialize geocoder with longer timeout
        geolocator = Nominatim(user_agent="measure_cases_locator_app", timeout=10)
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.5, max_retries=3)

        print("Geocoding addresses... This may take a while depending on the number of rows.")
        
        def fetch_coords(row):
            parts = []
            
            # Simple Address Construction: Street, Colony, Locality, State, Country
            
            # Street
            if pd.notna(row.get('Dirección')) and str(row.get('Dirección')).strip():
                parts.append(str(row.get('Dirección')).strip())
            
            # Colony
            if pd.notna(row.get('COLONIA')) and str(row.get('COLONIA')).strip():
                parts.append(str(row.get('COLONIA')).strip())
            
            # Locality (City) - Prefer 'Localidad' over 'Municipio' for geocoding city level
            if pd.notna(row.get('Localidad de residencia')) and str(row.get('Localidad de residencia')).strip():
                 parts.append(str(row.get('Localidad de residencia')).strip())
            elif pd.notna(row.get('Municipio de residencia')) and str(row.get('Municipio de residencia')).strip():
                 parts.append(str(row.get('Municipio de residencia')).strip())

            # Postal Code - Optional, sometimes confuses Nominatim if generic, but good for specific
            if pd.notna(row.get('Código Postal')):
                parts.append(str(int(row.get('Código Postal'))))

            parts.append("Durango")
            parts.append("Mexico")
            
            full_address = ", ".join(parts)
            print(f"Geocoding: {full_address}")
            
            try:
                location = geocode(full_address)
                if location:
                    return pd.Series([location.latitude, location.longitude])
            except (GeocoderTimedOut, GeocoderServiceError) as e:
                print(f"Bailed on {full_address} due to timeout/error: {e}")
            except Exception as e:
                print(f"Error on {full_address}: {e}")
            
            return pd.Series([None, None])

        # Apply to DataFrame and create new columns
        df[['Latitud_Calc', 'Longitud_Calc']] = df.apply(fetch_coords, axis=1)

        print("Saving to new Excel file...")
        df.to_excel(output_file, index=False)
        print(f"Done! Saved to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_coordinates()
